# Model previews

The manufacturer galleries show one labeled image for each model or assembly directory. Each image is rendered from a bundled model entry with MuJoCo 3.16.0 at 640 × 480 pixels, including the caption. The model page links `preview.json`, which records the exact entry, rendering method, joint pose and camera.

## Rendering methods

Native MJCF entries are loaded with MuJoCo. The renderer selects the `home` keyframe when present, otherwise the first keyframe or the model's default configuration. Demonstration scene entries are secondary to robot entries.

For URDF entries, yourdfpy 0.0.60 loads the visual geometry, materials and textures and computes link transforms. The preview loader converts declared mesh-file length units to metres, including file-local transforms, before applying URDF origins and joint transforms. Independent joints use the initial positions declared in `ros2_control`, or zero when none are supplied, clipped to their limits; mimic joints follow their specified relationships. The resulting surfaces are placed in a static MuJoCo scene for rendering. This preview scene contains the robot's appearance at that pose. The original URDF files and physical definitions remain the runtime assets.

A neutral floor, lights and a fitted camera are added for the image. The caption identifies the model. The selected entry is representative of its model directory; additional gripper, hardware and format variants are listed in the model's entry table.

## Regenerate the galleries

Python 3.12 and an OpenGL context are required. The published images were rendered on macOS arm64. Install the maintenance dependencies from the repository root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements-preview.txt
```

Render one model, or render every model by omitting `--model`:

```sh
.venv/bin/python scripts/render_previews.py --model franka/panda
.venv/bin/python scripts/render_previews.py --jobs 2
.venv/bin/python scripts/build_catalog.py
```

`--model` accepts a `manufacturer/model` directory and may be repeated. `--report /path/to/report.json` writes batch results outside the model directories. The catalog builder reads the model README entry tables and maintains both root language editions and all manufacturer galleries.

## Sources and licensing

Previews depict the entry named in their rendering record. Its source, license and attribution are recorded in the adjacent model README and accompanying format directory. Those terms also govern reuse of the depicted model resources. Universal Robots previews display the manufacturer's copyright attribution.

## Known limitations

Images establish the displayed geometry and pose. They do not establish dynamic stability, collision accuracy, controller performance or training behavior. The static URDF visualization does not constitute native MuJoCo physics support for that URDF. Material appearance depends on the source assets and the renderer; previews are not product photographs. Models with several variants have one representative image, with the selected variant identified in the rendering record.
