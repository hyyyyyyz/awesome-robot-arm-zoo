"""Stage composed USD visual meshes in MuJoCo for static catalog images."""

from pathlib import Path

import mujoco
import numpy as np
from pxr import Usd, UsdGeom, UsdShade
import trimesh


def _color(prim):
    material = UsdShade.MaterialBindingAPI(prim).ComputeBoundMaterial()[0]
    if material:
        for child in material.GetPrim().GetChildren():
            for name in ("inputs:diffuse_color_constant", "inputs:diffuseColor"):
                value = child.GetAttribute(name).Get()
                if value is not None:
                    return [*value, 1.0]
    colors = UsdGeom.Gprim(prim).GetDisplayColorAttr().Get()
    return [*colors[0], 1.0] if colors else [0.7, 0.7, 0.7, 1.0]


def build_usd_scene(entry: Path):
    """Render visual meshes at authored transforms, without simulating USD physics.

    Material colors are read from USD display colors or constant diffuse shader
    inputs. MDL execution, textures, sensors and collision guides are omitted.
    """
    stage = Usd.Stage.Open(str(Path(entry).resolve()))
    if stage is None:
        raise ValueError(f"Cannot compose USD stage: {entry}")
    scale = UsdGeom.GetStageMetersPerUnit(stage)
    transforms = UsdGeom.XformCache()
    spec = mujoco.MjSpec()
    spec.modelname = Path(entry).stem + "_visual_preview"
    all_bounds = []
    for prim in Usd.PrimRange.Stage(stage, Usd.TraverseInstanceProxies()):
        if not prim.IsA(UsdGeom.Mesh):
            continue
        imageable = UsdGeom.Imageable(prim)
        if (imageable.ComputeVisibility() == UsdGeom.Tokens.invisible or
                imageable.ComputePurpose() not in (UsdGeom.Tokens.default_, UsdGeom.Tokens.render)):
            continue
        mesh = UsdGeom.Mesh(prim)
        counts = np.asarray(mesh.GetFaceVertexCountsAttr().Get())
        if not np.all(counts == 3):
            raise ValueError(f"Preview requires triangular USD meshes: {prim.GetPath()}")
        points = np.asarray(mesh.GetPointsAttr().Get(), dtype=float)
        faces = np.asarray(mesh.GetFaceVertexIndicesAttr().Get(), dtype=np.int32).reshape(-1, 3)
        matrix = np.asarray(transforms.GetLocalToWorldTransform(prim)).T
        points = (points @ matrix[:3, :3].T + matrix[:3, 3]) * scale
        if UsdGeom.GetStageUpAxis(stage) == UsdGeom.Tokens.y:
            points = points[:, [0, 2, 1]] * [1, -1, 1]
        subsets = UsdGeom.Subset.GetGeomSubsets(mesh, UsdGeom.Tokens.face)
        groups = [(subset.GetPrim(), np.asarray(subset.GetIndicesAttr().Get(), dtype=int))
                  for subset in subsets]
        assigned = np.concatenate([indices for _, indices in groups]) if groups else []
        remaining = np.setdiff1d(np.arange(len(faces)), assigned)
        if len(remaining):
            groups.append((prim, remaining))
        for material_prim, indices in groups:
            surface = trimesh.Trimesh(vertices=points, faces=faces[indices], process=False)
            surface.remove_unreferenced_vertices()
            if not len(surface.faces) or surface.area <= mujoco.mjMINVAL:
                continue
            name = f"visual_{len(all_bounds)}"
            center = surface.vertices.mean(axis=0)
            vertices = np.asarray(surface.vertices - center, dtype=np.float32)
            if len(vertices) == 3:
                vertices = np.vstack((vertices, vertices[:1]))
            spec.add_mesh(
                name=name, uservert=vertices.ravel(),
                userface=np.asarray(surface.faces, dtype=np.int32).ravel(),
                usernormal=np.asarray(surface.vertex_normals, dtype=np.float32).ravel(),
                userfacenormal=np.asarray(surface.faces, dtype=np.int32).ravel(),
                inertia=mujoco.mjtMeshInertia.mjMESH_INERTIA_SHELL, maxhullvert=64,
            )
            spec.worldbody.add_geom(
                name=name, type=mujoco.mjtGeom.mjGEOM_MESH, meshname=name,
                pos=center, rgba=_color(material_prim), contype=0, conaffinity=0, group=2,
            )
            all_bounds.append(surface.bounds)
    if not all_bounds:
        raise ValueError(f"No visible USD meshes: {entry}")
    bounds = np.asarray(all_bounds)
    return spec, np.array([bounds[:, 0].min(axis=0), bounds[:, 1].max(axis=0)]), "authored USD transforms"
