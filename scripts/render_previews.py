"""Render a labeled MuJoCo preview for each documented robot model."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import itertools
import json
import logging
from pathlib import Path
import re
import subprocess
import sys

import mujoco
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
WIDTH, HEIGHT, CAPTION = 640, 432, 48


def model_entries(model_dir):
    """Select a documented robot entry, preferring native MJCF."""
    text = (model_dir / "README.md").read_text()
    section = text.split("## Model entries", 1)[1].split("\n## ", 1)[0]
    entries = {}
    for row in section.splitlines():
        match = re.search(r"\[`(models/[^`]+\.(?:urdf|xml|usd|usda|usdc))`\]", row)
        if match:
            path = match.group(1)
            purpose = row.split("|")[1].lower()
            entries[path] = "scene" in purpose or "demonstration" in purpose
    if not entries:
        raise ValueError(f"No documented entry in {model_dir}")
    paths = sorted(entries, key=lambda path: (
        entries[path],
        Path(path).suffix != ".xml",
        "scene" in Path(path).stem.lower(),
        "gripper" in Path(path).stem.lower(),
    ))
    return ROOT / paths[0]


def native_bounds(model, data):
    points = []
    signs = np.array(list(itertools.product([-1, 1], repeat=3)))
    for idx in range(model.ngeom):
        if model.geom_type[idx] == mujoco.mjtGeom.mjGEOM_PLANE:
            continue
        if model.geom_group[idx] > 2 or model.geom_rgba[idx, 3] == 0:
            continue
        center, half = model.geom_aabb[idx].reshape(2, 3)
        corners = center + signs * half
        rotation = data.geom_xmat[idx].reshape(3, 3)
        points.extend(corners @ rotation.T + data.geom_xpos[idx])
    vertices = np.asarray(points)
    return np.array([vertices.min(axis=0), vertices.max(axis=0)])


def native_scene(entry):
    spec = mujoco.MjSpec.from_file(str(entry))
    model = spec.compile()
    data = mujoco.MjData(model)
    pose = "default qpos0"
    key = -1
    if model.nkey:
        home = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_KEY, "home")
        key = home if home >= 0 else 0
        mujoco.mj_resetDataKeyframe(model, data, key)
        pose = "keyframe: " + (mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_KEY, key) or str(key))
    mujoco.mj_forward(model, data)
    return spec, native_bounds(model, data), pose, key


def add_studio(spec, bounds):
    center = bounds.mean(axis=0)
    span = max(float(np.max(bounds[1] - bounds[0])), 0.1)
    spec.visual.global_.offwidth = WIDTH
    spec.visual.global_.offheight = HEIGHT
    spec.visual.global_.fovy = 45
    spec.visual.quality.shadowsize = 2048
    spec.visual.headlight.ambient = [0.25, 0.25, 0.25]
    spec.visual.headlight.diffuse = [0.4, 0.4, 0.4]
    spec.visual.headlight.specular = [0.15, 0.15, 0.15]
    spec.worldbody.add_geom(
        name="gallery_floor", type=mujoco.mjtGeom.mjGEOM_PLANE,
        size=[0, 0, 0.01],
        pos=[center[0], center[1], bounds[0, 2] - span * 0.005],
        rgba=[0.78, 0.81, 0.85, 1], contype=0, conaffinity=0,
    )
    spec.worldbody.add_light(
        name="gallery_key", pos=center + span * np.array([1, -2, 3]),
        dir=[-0.3, 0.5, -1], type=mujoco.mjtLightType.mjLIGHT_DIRECTIONAL,
        diffuse=[0.35, 0.35, 0.35], castshadow=True,
    )
    camera = mujoco.MjvCamera()
    camera.lookat[:] = center
    camera.azimuth = 135
    camera.elevation = -25
    camera.distance = max(float(np.linalg.norm(bounds[1] - bounds[0])) * 1.25, 0.2)
    return camera


def caption_image(pixels, title, brand):
    image = Image.new("RGB", (WIDTH, HEIGHT + CAPTION), "#f7f9fb")
    image.paste(Image.fromarray(pixels), (0, 0))
    draw = ImageDraw.Draw(image)
    size = 19
    font = ImageFont.load_default(size=size)
    while draw.textbbox((0, 0), title, font=font)[2] > WIDTH - 28 and size > 11:
        size -= 1
        font = ImageFont.load_default(size=size)
    draw.text((14, HEIGHT + 8), title, fill="#162b40", font=font)
    label = "MuJoCo 3.16 · model preview"
    if brand == "universal_robots":
        label += " · © Universal Robots A/S"
    draw.text((14, HEIGHT + 30), label, fill="#566b7f", font=ImageFont.load_default(size=11))
    return image


def fit_camera(renderer, model, data, camera, options, floor_id):
    """Frame visible robot surfaces, including meshes with distant CAD points."""
    floor_ids = np.flatnonzero(model.geom_type == mujoco.mjtGeom.mjGEOM_PLANE)
    renderer.update_scene(data, camera=camera, scene_option=options)
    renderer.enable_segmentation_rendering()
    segmentation = renderer.render()
    mask = (segmentation[:, :, 0] >= 0) & ~np.isin(segmentation[:, :, 0], floor_ids)
    yy, xx = np.nonzero(mask)
    if not len(xx):
        raise ValueError("No visible robot surfaces in initial frame")
    renderer.disable_segmentation_rendering()
    renderer.enable_depth_rendering()
    depth = renderer.render()[mask]
    renderer.disable_depth_rendering()
    median_depth = float(np.median(depth))
    glcamera = renderer.scene.camera[0]
    position = (renderer.scene.camera[0].pos + renderer.scene.camera[1].pos) / 2
    forward = np.asarray(glcamera.forward)
    up = np.asarray(glcamera.up)
    right = np.cross(forward, up)
    tangent = np.tan(np.deg2rad(45 / 2))
    horizontal = (xx - WIDTH / 2) * 2 / HEIGHT
    vertical = (HEIGHT / 2 - yy) * 2 / HEIGHT
    surfaces = position + depth[:, None] * (
        forward + tangent * (horizontal[:, None] * right + vertical[:, None] * up))
    visible_span = float(np.max(np.ptp(surfaces, axis=0)))
    model.geom_pos[floor_id, 2] = float(surfaces[:, 2].min()) - visible_span * 0.01
    mujoco.mj_forward(model, data)
    x_offset = ((xx.min() + xx.max()) / 2 - WIDTH / 2) * 2 / HEIGHT
    y_offset = (HEIGHT / 2 - (yy.min() + yy.max()) / 2) * 2 / HEIGHT
    camera.lookat[:] = position + median_depth * (
        forward + tangent * (right * x_offset + up * y_offset))
    fill = max((xx.max() - xx.min() + 1) / (WIDTH * 0.70),
               (yy.max() - yy.min() + 1) / (HEIGHT * 0.72))
    camera.distance = median_depth * fill + float(median_depth - depth.min())
    renderer.enable_segmentation_rendering()
    for _ in range(4):
        renderer.update_scene(data, camera=camera, scene_option=options)
        segmentation = renderer.render()
        yy, xx = np.nonzero((segmentation[:, :, 0] >= 0) &
                            ~np.isin(segmentation[:, :, 0], floor_ids))
        if not len(xx):
            raise ValueError("No visible robot surfaces after camera fitting")
        bounds = [int(xx.min()), int(yy.min()), int(xx.max()), int(yy.max())]
        if bounds[0] >= 12 and bounds[1] >= 12 and bounds[2] < WIDTH - 12 and bounds[3] < HEIGHT - 12:
            renderer.disable_segmentation_rendering()
            return bounds
        camera.distance *= 1.2
    raise ValueError("Robot does not fit within the preview margins")


def render_model(model_dir):
    entry = model_entries(model_dir)
    title = (model_dir / "README.md").read_text().splitlines()[0].lstrip("# ")
    if entry.suffix == ".urdf":
        from preview_urdf import build_urdf_scene
        spec, bounds, pose = build_urdf_scene(entry)
        method = "URDF visual geometry and forward kinematics rendered in a static MuJoCo scene"
        key = -1
    elif entry.suffix in (".usd", ".usda", ".usdc"):
        from preview_usd import build_usd_scene
        spec, bounds, pose = build_usd_scene(entry)
        method = "USD composed visual meshes at authored transforms rendered in a static MuJoCo scene"
        key = -1
    else:
        spec, bounds, pose, key = native_scene(entry)
        method = "Native MJCF loaded in MuJoCo"
    camera = add_studio(spec, bounds)
    model = spec.compile()
    data = mujoco.MjData(model)
    if key >= 0:
        mujoco.mj_resetDataKeyframe(model, data, key)
    mujoco.mj_forward(model, data)
    options = mujoco.MjvOption()
    options.geomgroup[3:] = 0
    with mujoco.Renderer(model, height=HEIGHT, width=WIDTH) as renderer:
        floor_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_GEOM, "gallery_floor")
        pixel_bounds = fit_camera(renderer, model, data, camera, options, floor_id)
        pixels = renderer.render()
    image = caption_image(pixels, title, model_dir.parent.name)
    image.save(model_dir / "preview.png", optimize=True)
    record = {
        "entry": str(entry.relative_to(ROOT)), "renderer": f"MuJoCo {mujoco.__version__}",
        "method": method, "pose": pose,
        "camera": {"azimuth": camera.azimuth, "elevation": camera.elevation,
                   "distance": camera.distance, "lookat": camera.lookat.tolist()},
        "image": "preview.png", "size": list(image.size),
        "robot_pixel_bounds": pixel_bounds,
    }
    (model_dir / "preview.json").write_text(json.dumps(record, indent=2) + "\n")
    return record


def run_worker(model_dir):
    result = subprocess.run(
        [sys.executable, str(Path(__file__).resolve()), "--worker", str(model_dir)],
        capture_output=True, text=True, timeout=300,
    )
    label = str(model_dir.relative_to(ROOT))
    if result.returncode:
        return {"model": label, "status": "failed", "error": result.stderr[-2500:]}
    return {"model": label, "status": "rendered"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", action="append", help="Brand/model path; repeat to select several")
    parser.add_argument("--worker", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--jobs", type=int, default=2)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    logging.basicConfig(level=logging.ERROR)
    if args.worker:
        render_model(args.worker.resolve())
        return
    models = ([ROOT / "models" / name for name in args.model] if args.model else
              [path.parent for path in sorted((ROOT / "models").glob("*/*/README.md"))])
    results = []
    with ThreadPoolExecutor(max_workers=args.jobs) as executor:
        for result in executor.map(run_worker, models):
            results.append(result)
            print(json.dumps(result), flush=True)
            if args.report:
                args.report.parent.mkdir(parents=True, exist_ok=True)
                args.report.write_text(json.dumps(results, indent=2) + "\n")
    if any(result["status"] == "failed" for result in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
