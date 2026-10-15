# Lebai TWO LM3

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Lebai TWO LM3 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Two LM3 6-joint arms without grippers, on the supplied fixed mounting arrangement. The entry preserves the upstream kinematic, visual, collision, inertial and joint-limit definitions.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Complete assembly: Two LM3 6-joint arms without grippers, on the supplied fixed mounting arrangement | URDF | [`models/lebai/two_lm3/urdf/two_lm3.urdf`](urdf/two_lm3.urdf) | A native URDF loader with relative mesh resolution; attach the base to the consuming scene. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | Two LM3 6-joint arms without grippers, on the supplied fixed mounting arrangement |
| Units | Metres, kilograms, radians; revolute joint effort in N·m and prismatic effort in N. Mesh scale attributes remain as supplied upstream. |
| Base | `world`; root of the URDF tree. Any supplied fixed base transform is retained. |
| Arm joint order | Robot 1: `robot1_joint_1` → `robot1_joint_2` → `robot1_joint_3` → `robot1_joint_4` → `robot1_joint_5` → `robot1_joint_6`; robot 2: `robot2_joint_1` → `robot2_joint_2` → `robot2_joint_3` → `robot2_joint_4` → `robot2_joint_5` → `robot2_joint_6`. |
| Gripper | No gripper is included. |
| End effector / TCP | `robot1_tool0`, `robot2_tool0`; fixed transforms remain in the entry. |
| Included poses | No named poses are defined by this URDF entry. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/lebai/two_lm3/urdf/two_lm3.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Static URDF and its bundled resources (lebai_lm3_support) | [https://github.com/lebai-robotics/lebai-ros-sdk](https://github.com/lebai-robotics/lebai-ros-sdk) | `f1f13b6849f34f61dce0483e09f531816d292b63` | `lebai_lm3_support/urdf/two_lm3.xacro`; model mesh paths under the named packages | [LICENSE](urdf/LICENSE) |

Bundled upstream resource directories: `lebai_lm3_support/meshes/lm3/collision`, `lebai_lm3_support/meshes/lm3/visual`.

License scope: Apache-2.0 for lebai_lm3_support and lebai_resources, including their mesh resources. The complete upstream license texts and notices accompany this format directory.

## Model preparation

The static entry was expanded with xacro 2.1.1 using upstream defaults. Resources were copied only when referenced by the entry or by one of its mesh/material files. Resource references are local relative paths. Mesh contents and physical parameters retain the upstream definitions. The upstream jazzy-dev description and common material macros supply all mechanical definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/lebai/two_lm3/urdf/two_lm3.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

ROS, Gazebo and physics simulators have not been verified for this entry. Gripper and robot controller connections have not been verified.
