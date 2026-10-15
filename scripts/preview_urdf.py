"""Stage URDF visual geometry in MuJoCo for static catalog images."""

import logging
from pathlib import Path
import xml.etree.ElementTree as ET

import mujoco
import numpy as np
import trimesh
import yourdfpy


class _MeterVisualURDF(yourdfpy.URDF):
    """Apply resource units before visual origins and robot joint transforms."""

    def _geometry2trimeshscene(self, geometry, load_file, force_mesh, skip_materials):
        scene = super()._geometry2trimeshscene(
            geometry, load_file, force_mesh, skip_materials
        )
        if scene is not None and geometry.mesh is not None:
            units = {mesh.metadata.get("units", "meters") for mesh in scene.geometry.values()}
            if len(units) == 1:
                factor = trimesh.units.unit_conversion(units.pop(), "meters")
                if factor != 1:
                    scene = scene.scaled(factor)
        return scene


def _appearance(mesh: trimesh.Trimesh):
    """Return material properties and explicit texture-coordinate indices."""
    visual = mesh.visual
    rgba = np.ones(4)
    image = None
    uv = None
    uv_faces = None
    material_options = {"specular": 0.08, "shininess": 0.2}

    if isinstance(visual, trimesh.visual.TextureVisuals):
        material = visual.material
        if isinstance(material, trimesh.visual.material.PBRMaterial):
            if material.baseColorFactor is not None:
                rgba = np.asarray(material.baseColorFactor, dtype=float) / 255
            image = material.baseColorTexture
            if material.metallicFactor is not None:
                material_options["metallic"] = float(material.metallicFactor)
            if material.roughnessFactor is not None:
                roughness = float(material.roughnessFactor)
                material_options["roughness"] = roughness
                material_options["shininess"] = 1 - roughness
            if material.emissiveFactor is not None:
                material_options["emission"] = float(np.mean(material.emissiveFactor))
        elif isinstance(material, trimesh.visual.material.SimpleMaterial):
            rgba = np.asarray(material.diffuse, dtype=float) / 255
            image = material.image
        uv = visual.uv
        if uv is not None:
            uv_faces = mesh.faces
    elif isinstance(visual, trimesh.visual.ColorVisuals):
        colors = visual.face_colors if visual.kind == "face" else visual.vertex_colors
        if np.all(colors == colors[0]):
            rgba = np.asarray(colors[0], dtype=float) / 255
        else:
            material, uv = trimesh.visual.color.color_to_uv(colors)
            image = material.image
            uv_faces = (
                np.repeat(np.arange(len(mesh.faces))[:, None], 3, axis=1)
                if visual.kind == "face"
                else mesh.faces
            )

    return rgba, image, uv, uv_faces, material_options


def build_urdf_scene(entry: Path):
    """Return a static visual spec, world bounds, and the displayed joint pose.

    The original URDF remains the runtime model. This scene contains its visual
    surfaces at declared initial joint positions, or zero, clipped to limits;
    it has no robot dynamics.
    Mimic joints are positioned by yourdfpy's forward kinematics. Resource units
    are converted to meters. Surfaces below MuJoCo's minimum area are omitted.
    """
    entry = Path(entry).resolve()
    description = yourdfpy.URDF.load(str(entry), build_scene_graph=False, load_meshes=False)
    robot = _MeterVisualURDF(
        robot=description.robot, mesh_dir=str(entry.parent),
        build_scene_graph=True,
        load_meshes=True,
        build_collision_scene_graph=False,
        load_collision_meshes=False,
        force_mesh=False,
    )
    initial_positions = {}
    for joint in ET.parse(entry).getroot().findall("ros2_control/joint"):
        parameter = joint.find("state_interface[@name='position']/param[@name='initial_value']")
        if parameter is not None and parameter.text is not None:
            try:
                value = float(parameter.text)
            except ValueError:
                continue
            if np.isfinite(value):
                initial_positions[joint.get("name")] = value
    pose = {}
    for joint in robot.actuated_joints:
        if joint.type in ("revolute", "continuous", "prismatic"):
            lower = joint.limit.lower if joint.limit is not None else None
            upper = joint.limit.upper if joint.limit is not None else None
            pose[joint.name] = float(
                np.clip(initial_positions.get(joint.name, 0.0),
                        lower if lower is not None else -np.inf,
                        upper if upper is not None else np.inf)
            )
    robot.update_cfg(pose)
    scene = robot.scene
    if not scene.geometry:
        raise ValueError(f"URDF has no loaded visual geometry: {entry}")

    spec = mujoco.MjSpec()
    spec.modelname = Path(entry).stem + "_visual_preview"
    spec.compiler.inertiafromgeom = mujoco.mjtInertiaFromGeom.mjINERTIAFROMGEOM_FALSE
    material_names = {}
    texture_pixels = {}
    for index, node in enumerate(scene.graph.nodes_geometry):
        transform, geometry_name = scene.graph.get(node)
        mesh = scene.geometry[geometry_name].copy()
        mesh.apply_transform(transform)
        if not len(mesh.faces) or mesh.area <= mujoco.mjMINVAL:
            logging.warning(
                "Omitting preview surface %s with area %.6g m² in %s",
                node, mesh.area, entry,
            )
            continue
        name = f"visual_{index}"
        rgba, texture_image, uv, uv_faces, material_options = _appearance(mesh)
        # Local coordinates retain small CAD triangles when MuJoCo stores float32.
        position = mesh.vertices.mean(axis=0)
        vertices = np.asarray(mesh.vertices - position, dtype=np.float32)
        if len(vertices) == 3:
            # MuJoCo requires four stored vertices even for a single triangle.
            # An unreferenced duplicate preserves the rendered surface exactly.
            vertices = np.vstack((vertices, vertices[:1]))
        mesh_options = {
            "name": name,
            "uservert": vertices.ravel(),
            "userface": np.asarray(mesh.faces, dtype=np.int32).ravel(),
            "usernormal": np.asarray(mesh.vertex_normals, dtype=np.float32).ravel(),
            "userfacenormal": np.asarray(mesh.faces, dtype=np.int32).ravel(),
            "inertia": mujoco.mjtMeshInertia.mjMESH_INERTIA_SHELL,
            "maxhullvert": 64,
        }
        texture_name = ""
        if texture_image is not None and uv is not None:
            pixels = np.asarray(texture_image.convert("RGB"), dtype=np.uint8)
            candidates = texture_pixels.setdefault(pixels.shape, [])
            texture_name = next(
                (stored_name for stored_pixels, stored_name in candidates
                 if np.array_equal(stored_pixels, pixels)), ""
            )
            if not texture_name:
                texture_name = name + "_texture"
                spec.add_texture(
                    name=texture_name, type=mujoco.mjtTexture.mjTEXTURE_2D,
                    width=pixels.shape[1], height=pixels.shape[0], nchannel=3,
                    data=pixels.ravel(),
                )
                candidates.append((pixels, texture_name))
            textures = [""] * 10
            textures[mujoco.mjtTextureRole.mjTEXROLE_RGB] = texture_name
            material_options["textures"] = textures
            mesh_options["usertexcoord"] = np.asarray(uv, dtype=np.float32).ravel()
            mesh_options["userfacetexcoord"] = np.asarray(uv_faces, dtype=np.int32).ravel()
        material_key = (
            tuple(rgba), texture_name,
            tuple((key, value) for key, value in material_options.items() if key != "textures"),
        )
        material_name = material_names.get(material_key)
        if material_name is None:
            material_name = name + "_material"
            spec.add_material(name=material_name, rgba=rgba, **material_options)
            material_names[material_key] = material_name
        spec.add_mesh(**mesh_options)
        spec.worldbody.add_geom(
            name=name, type=mujoco.mjtGeom.mjGEOM_MESH, meshname=name,
            pos=position, material=material_name, contype=0, conaffinity=0, group=2,
        )
    return spec, np.asarray(scene.bounds), pose
