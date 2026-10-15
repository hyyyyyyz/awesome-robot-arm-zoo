# Han’s Robot / Huayan Robotics ELFIN15

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Han’s Robot / Huayan Robotics ELFIN15 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Elfin15 6-joint arm without a gripper. The entry preserves the upstream kinematic, visual, collision, inertial and joint-limit definitions.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model: Elfin15 6-joint arm without a gripper | URDF | [`models/hans_robot/elfin15/urdf/elfin15.urdf`](urdf/elfin15.urdf) | A native URDF loader with relative mesh resolution; attach the base to the consuming scene. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | Elfin15 6-joint arm without a gripper |
| Units | Metres, kilograms, radians; revolute joint effort in N·m and prismatic effort in N. Mesh scale attributes remain as supplied upstream. |
| Base | `world`; root of the URDF tree. Any supplied fixed base transform is retained. |
| Arm joint order | `elfin_joint1` → `elfin_joint2` → `elfin_joint3` → `elfin_joint4` → `elfin_joint5` → `elfin_joint6` |
| Gripper | No gripper is included. |
| End effector / TCP | `elfin_end_link` is the supplied arm attachment frame; `elfin_dummy_gripper` is a fixed, geometry-free helper frame. |
| Included poses | No named poses are defined by this URDF entry. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/hans_robot/elfin15/urdf/elfin15.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Static URDF and its bundled resources (elfin_description) | [https://github.com/huayan-robotics/elfin_robot](https://github.com/huayan-robotics/elfin_robot) | `1c642fbdcd6a2467084288fe373f945bc38a8c52` | `elfin_description/urdf/elfin15.urdf.xacro`; model mesh paths under the named packages | [LICENSE](urdf/LICENSE) |

Bundled upstream resource directories: `elfin_description/meshes/elfin15`.

License scope: BSD-3-Clause for the robot description and meshes; copyright 2017 Han’s Robot Co., Ltd. The complete upstream license texts and notices accompany this format directory.

## Model preparation

The static entry was expanded with xacro 2.1.1 using upstream defaults. Resources were copied only when referenced by the entry or by one of its mesh/material files. Resource references are local relative paths. Mesh contents and physical parameters retain the upstream definitions. The supplied fixed attachment and base-frame rotation are retained. Gazebo and transmission elements remain as source metadata.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/hans_robot/elfin15/urdf/elfin15.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

ROS, Gazebo and physics simulators have not been verified for this entry. Gazebo plugins and hardware interfaces have not been verified.
