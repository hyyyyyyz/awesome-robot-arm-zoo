# Elephant Robotics mycobot 320 pi 2022

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Elephant Robotics mycobot 320 pi 2022 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Official manufacturer model files for the assembly identified below.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model — arm | URDF | [`models/elephant_robotics/mycobot_320_pi_2022/urdf/arm/mycobot_320_pi_2022.urdf`](urdf/arm/mycobot_320_pi_2022.urdf) | Local file loader; use a fixed base for mounted arms. |
| Robot model — with_gripper | URDF | [`models/elephant_robotics/mycobot_320_pi_2022/urdf/with_gripper/mycobot_320_pi_2022.urdf`](urdf/with_gripper/mycobot_320_pi_2022.urdf) | Local file loader; use a fixed base for mounted arms. |
| Robot model — with_force_gripper | URDF | [`models/elephant_robotics/mycobot_320_pi_2022/urdf/with_force_gripper/mycobot_320_pi_2022.urdf`](urdf/with_force_gripper/mycobot_320_pi_2022.urdf) | Local file loader; use a fixed base for mounted arms. |

## Mechanical information

### arm

| Item | Definition |
|---|---|
| Hardware revision and gripper | Elephant Robotics mycobot 320 pi 2022; configuration represented by the entry. |
| Units | URDF SI conventions: metres, kilograms, radians. Mesh scaling is retained from upstream. |
| Base | `base`; attach this root frame to the consuming scene. |
| Movable joint order | `joint2_to_joint1`, `joint3_to_joint2`, `joint4_to_joint3`, `joint5_to_joint4`, `joint6_to_joint5`, `joint6output_to_joint6` (upstream declaration order; fixed joints omitted). |
| Gripper | No mimic coupling is declared. Any gripper joint limits remain in the entry. |
| End effector / TCP | Leaf frames: `link6`. Their upstream transforms are retained. |
| Included poses | No separate pose configuration is included. |
### with_gripper

| Item | Definition |
|---|---|
| Hardware revision and gripper | Elephant Robotics mycobot 320 pi 2022 with gripper; configuration represented by the entry. |
| Units | URDF SI conventions: metres, kilograms, radians. Mesh scaling is retained from upstream. |
| Base | `base`; attach this root frame to the consuming scene. |
| Movable joint order | `joint2_to_joint1`, `joint3_to_joint2`, `joint4_to_joint3`, `joint5_to_joint4`, `joint6_to_joint5`, `joint6output_to_joint6`, `gripper_controller`, `gripper_base_to_gripper_left2`, `gripper_left3_to_gripper_left1`, `gripper_base_to_gripper_right3`, `gripper_base_to_gripper_right2`, `gripper_right3_to_gripper_right1` (upstream declaration order; fixed joints omitted). |
| Gripper | gripper_base_to_gripper_left2 mimics gripper_controller (multiplier 1.0, offset 0); gripper_left3_to_gripper_left1 mimics gripper_controller (multiplier -1.0, offset 0); gripper_base_to_gripper_right3 mimics gripper_controller (multiplier -1.0, offset 0); gripper_base_to_gripper_right2 mimics gripper_controller (multiplier -1.0, offset 0); gripper_right3_to_gripper_right1 mimics gripper_controller (multiplier 1.0, offset 0) |
| End effector / TCP | Leaf frames: `gripper_left1`, `gripper_left2`, `gripper_right1`, `gripper_right2`. Their upstream transforms are retained. |
| Included poses | No separate pose configuration is included. |
### with_force_gripper

| Item | Definition |
|---|---|
| Hardware revision and gripper | Elephant Robotics mycobot 320 pi 2022 with force gripper; configuration represented by the entry. |
| Units | URDF SI conventions: metres, kilograms, radians. Mesh scaling is retained from upstream. |
| Base | `base`; attach this root frame to the consuming scene. |
| Movable joint order | `joint2_to_joint1`, `joint3_to_joint2`, `joint4_to_joint3`, `joint5_to_joint4`, `joint6_to_joint5`, `joint6output_to_joint6`, `gripper_controller`, `gripper_base_to_gripper_left2`, `gripper_left3_to_gripper_left1`, `gripper_base_to_gripper_right3`, `gripper_base_to_gripper_right2`, `gripper_right3_to_gripper_right1` (upstream declaration order; fixed joints omitted). |
| Gripper | gripper_base_to_gripper_left2 mimics gripper_controller (multiplier 1.0, offset 0); gripper_left3_to_gripper_left1 mimics gripper_controller (multiplier -1.0, offset 0); gripper_base_to_gripper_right3 mimics gripper_controller (multiplier -1.0, offset 0); gripper_base_to_gripper_right2 mimics gripper_controller (multiplier -1.0, offset 0); gripper_right3_to_gripper_right1 mimics gripper_controller (multiplier 1.0, offset 0) |
| End effector / TCP | Leaf frames: `gripper_left1`, `gripper_left2`, `gripper_right1`, `gripper_right2`. Their upstream transforms are retained. |
| Included poses | No separate pose configuration is included. |

### URDF / arm joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `joint2_to_joint1` | revolute | -2.93 | 2.93 | radians |
| `joint3_to_joint2` | revolute | -2.35 | 2.35 | radians |
| `joint4_to_joint3` | revolute | -2.53 | 2.53 | radians |
| `joint5_to_joint4` | revolute | -2.53 | 2.53 | radians |
| `joint6_to_joint5` | revolute | -2.93 | 2.93 | radians |
| `joint6output_to_joint6` | revolute | -3.14 | 3.14 | radians |

### URDF / with_gripper joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `joint2_to_joint1` | revolute | -2.93 | 2.93 | radians |
| `joint3_to_joint2` | revolute | -2.35 | 2.35 | radians |
| `joint4_to_joint3` | revolute | -2.53 | 2.53 | radians |
| `joint5_to_joint4` | revolute | -2.53 | 2.53 | radians |
| `joint6_to_joint5` | revolute | -2.93 | 2.93 | radians |
| `joint6output_to_joint6` | revolute | -3.14 | 3.14 | radians |
| `gripper_controller` | revolute | -0.7 | 0.3 | radians |
| `gripper_base_to_gripper_left2` | revolute | -0.8 | 0.5 | radians |
| `gripper_left3_to_gripper_left1` | revolute | -0.5 | 0.5 | radians |
| `gripper_base_to_gripper_right3` | revolute | -0.3 | 0.7 | radians |
| `gripper_base_to_gripper_right2` | revolute | -0.5 | 0.8 | radians |
| `gripper_right3_to_gripper_right1` | revolute | -0.5 | 0.5 | radians |

### URDF / with_force_gripper joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `joint2_to_joint1` | revolute | -2.93 | 2.93 | radians |
| `joint3_to_joint2` | revolute | -2.35 | 2.35 | radians |
| `joint4_to_joint3` | revolute | -2.53 | 2.53 | radians |
| `joint5_to_joint4` | revolute | -2.53 | 2.53 | radians |
| `joint6_to_joint5` | revolute | -2.93 | 2.93 | radians |
| `joint6output_to_joint6` | revolute | -3.14 | 3.14 | radians |
| `gripper_controller` | revolute | 0 | 1 | radians |
| `gripper_base_to_gripper_left2` | revolute | -0.8 | 0.5 | radians |
| `gripper_left3_to_gripper_left1` | revolute | -0.5 | 0.5 | radians |
| `gripper_base_to_gripper_right3` | revolute | 1 | 0 | radians |
| `gripper_base_to_gripper_right2` | revolute | -0.5 | 0.8 | radians |
| `gripper_right3_to_gripper_right1` | revolute | -0.5 | 0.5 | radians |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/elephant_robotics/mycobot_320_pi_2022/urdf/arm/mycobot_320_pi_2022.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF / arm entry and referenced resources | [mycobot_ros](https://github.com/elephantrobotics/mycobot_ros) | `c0d6fbe8f7d9b18b46a9fcb0b041e5bc2d66196b` | `mycobot_description/urdf/mycobot_320_pi_2022/new_mycobot_pro_320_pi_2022.urdf` | [LICENSE](urdf/arm/LICENSE), [NOTICES](urdf/arm/NOTICES) |
| URDF / with_gripper entry and referenced resources | [mycobot_ros](https://github.com/elephantrobotics/mycobot_ros) | `c0d6fbe8f7d9b18b46a9fcb0b041e5bc2d66196b` | `mycobot_description/urdf/mycobot_320_pi_2022/new_mycobot_pro_320_pi_2022_gripper.urdf` | [LICENSE](urdf/with_gripper/LICENSE), [NOTICES](urdf/with_gripper/NOTICES) |
| URDF / with_force_gripper entry and referenced resources | [mycobot_ros](https://github.com/elephantrobotics/mycobot_ros) | `c0d6fbe8f7d9b18b46a9fcb0b041e5bc2d66196b` | `mycobot_description/urdf/mycobot_320_pi_2022/pro_320_pi_2022_force_gripper.urdf` | [LICENSE](urdf/with_force_gripper/LICENSE), [NOTICES](urdf/with_force_gripper/NOTICES) |

License: BSD-3-Clause. The license and attribution notices apply to the model entry and copied dependencies from the stated project.

## Model preparation

The upstream README identifies the repository license as BSD-3-Clause, copyright 2020–2023 Elephant Robotics. Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

The upstream README identifies the repository license as BSD-3-Clause, copyright 2020–2023 Elephant Robotics. Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

The upstream README identifies the repository license as BSD-3-Clause, copyright 2020–2023 Elephant Robotics. Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/elephant_robotics/mycobot_320_pi_2022/urdf/arm/mycobot_320_pi_2022.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |
| `models/elephant_robotics/mycobot_320_pi_2022/urdf/with_gripper/mycobot_320_pi_2022.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |
| `models/elephant_robotics/mycobot_320_pi_2022/urdf/with_force_gripper/mycobot_320_pi_2022.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Bundled COLLADA meshes declare length units in their asset metadata. The plain yourdfpy 0.0.60 / trimesh 5.1.1 loader does not apply those units; the preview renderer applies them to meshes and file-local transforms. Consuming loaders must honor the declared units. Recorded loading checks cover resource resolution and joint configuration updates, not dimensional accuracy.

Dynamic task execution, controller performance and training behavior have not been validated.

- ROS and Gazebo control extensions, when present, retain their upstream metadata; their external runtime plugins are not included.
- Upstream hardware or revision distinctions beyond the source filename are not independently established.
- The URDF has no inertial element for `base`, `link1`, `link2`, `link3`, `link4`, `link5`, `link6`.
- The URDF has no inertial element for `base`, `link1`, `link2`, `link3`, `link4`, `link5`, `link6`, `gripper_base`, `gripper_left1`, `gripper_left2`, `gripper_left3`, `gripper_right1`, `gripper_right2`, `gripper_right3`.
- The URDF has no inertial element for `base`, `link1`, `link2`, `link3`, `link4`, `link5`, `link6`, `gripper_connection`, `gripper_base`, `gripper_left1`, `gripper_left2`, `gripper_left3`, `gripper_right1`, `gripper_right2`, `gripper_right3`.
