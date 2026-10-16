# Seeed Studio reBot DevArm (RobStride)

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Seeed Studio reBot DevArm (RobStride) model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Six-axis open-source arm with a rack-and-pinion parallel gripper. This entry uses the RobStride RS-06 / RS-00 actuator assembly.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Fixed-base arm and parallel gripper | MJCF | [`models/seeed_studio/rebot_devarm_rs/mjcf/seeed_rebot_devarm.xml`](mjcf/seeed_rebot_devarm.xml) | MuJoCo 3.2.0 or later. |
| Arm with demonstration floor and lighting | MJCF | [`models/seeed_studio/rebot_devarm_rs/mjcf/scene.xml`](mjcf/scene.xml) | MuJoCo 3.2.0 or later; scene includes the same arm. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | reBot DevArm with RobStride RS-06 shoulder/elbow and RS-00 wrist/gripper actuators. |
| Units | Metres, kilograms, radians. Finger joint displacements are metres. |
| Base | `base_link`, fixed to the world. |
| Arm joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`. |
| Gripper relationships | `joint_left` and `joint_right` are coupled by the upstream 1:1 equality constraint. Both position actuators are retained. |
| End effector / TCP | `gripper_end` body; no additional TCP offset is introduced. |
| Included poses | `home` and `raised` keyframes. |

## Loading example

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/seeed_studio/rebot_devarm_rs/mjcf/seeed_rebot_devarm.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Curated MJCF, original meshes and decomposed collision meshes | [Google DeepMind MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `seeed_rebot_devarm/` | [MIT](mjcf/LICENSE), [attribution](mjcf/NOTICES) |

The curator derives geometry and physical parameters from [Seeed Studio's reBot-Isaacsim](https://github.com/Seeed-Projects/reBot-Isaacsim). Its model-specific MIT license is retained. This is a curated model derived from the official model, rather than a manufacturer-authored MJCF.

## Model preparation

The MJCF files and referenced meshes are copied without physical changes. The source fixes the base, retains full link inertias, defines position actuators and uses convex-decomposition collision meshes. Its contact exclusions, actuator gains, gripper coupling and keyframes are retained. The [curator's model notes](https://github.com/google-deepmind/mujoco_menagerie/blob/6da8b971844845de6ab27315aacc3a3fea4ddb8e/seeed_rebot_devarm/README.md) describe these definitions.

## Loading verification

Checked on 2026-10-16 with MuJoCo 3.16.0, macOS 27.2 arm64 and Python 3.12.14. Both `seeed_rebot_devarm.xml` and `scene.xml` compiled, created `MjData` and completed `mj_forward`. Each absolute entry loaded from a different working directory after copying the complete `mjcf/` directory to a temporary location. Result: both passed, including resource relocation.

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated. This RobStride assembly is distinct from DevArm variants using other actuators.
