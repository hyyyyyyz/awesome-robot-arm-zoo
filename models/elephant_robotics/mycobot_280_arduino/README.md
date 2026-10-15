# Elephant Robotics mycobot 280 arduino

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Elephant Robotics mycobot 280 arduino model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Official manufacturer model files for the assembly identified below.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model — arm | URDF | [`models/elephant_robotics/mycobot_280_arduino/urdf/arm/mycobot_280_arduino.urdf`](urdf/arm/mycobot_280_arduino.urdf) | Local file loader; use a fixed base for mounted arms. |

## Mechanical information

### arm

| Item | Definition |
|---|---|
| Hardware revision and gripper | Elephant Robotics mycobot 280 arduino; configuration represented by the entry. |
| Units | URDF SI conventions: metres, kilograms, radians. Mesh scaling is retained from upstream. |
| Base | `joint1`; attach this root frame to the consuming scene. |
| Movable joint order | `joint2_to_joint1`, `joint3_to_joint2`, `joint4_to_joint3`, `joint5_to_joint4`, `joint6_to_joint5`, `joint6output_to_joint6` (upstream declaration order; fixed joints omitted). |
| Gripper | No mimic coupling is declared. Any gripper joint limits remain in the entry. |
| End effector / TCP | Leaf frames: `joint6_flange`. Their upstream transforms are retained. |
| Included poses | No separate pose configuration is included. |

### URDF / arm joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `joint2_to_joint1` | revolute | -2.9321 | 2.9321 | radians |
| `joint3_to_joint2` | revolute | -2.4434 | 2.4434 | radians |
| `joint4_to_joint3` | revolute | -2.6179 | 2.6179 | radians |
| `joint5_to_joint4` | revolute | -2.6179 | 2.6179 | radians |
| `joint6_to_joint5` | revolute | -2.7052 | 2.7925 | radians |
| `joint6output_to_joint6` | revolute | -3.14 | 3.14159 | radians |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/elephant_robotics/mycobot_280_arduino/urdf/arm/mycobot_280_arduino.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF / arm entry and referenced resources | [mycobot_ros](https://github.com/elephantrobotics/mycobot_ros) | `c0d6fbe8f7d9b18b46a9fcb0b041e5bc2d66196b` | `mycobot_description/urdf/mycobot_280_arduino/mycobot_280_arduino.urdf` | [LICENSE](urdf/arm/LICENSE), [NOTICES](urdf/arm/NOTICES) |

License: BSD-3-Clause. The license and attribution notices apply to the model entry and copied dependencies from the stated project.

## Model preparation

The upstream README identifies the repository license as BSD-3-Clause, copyright 2020–2023 Elephant Robotics. Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/elephant_robotics/mycobot_280_arduino/urdf/arm/mycobot_280_arduino.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Bundled COLLADA meshes declare length units in their asset metadata. The plain yourdfpy 0.0.60 / trimesh 5.1.1 loader does not apply those units; the preview renderer applies them to meshes and file-local transforms. Consuming loaders must honor the declared units. Recorded loading checks cover resource resolution and joint configuration updates, not dimensional accuracy.

Dynamic task execution, controller performance and training behavior have not been validated.

- ROS and Gazebo control extensions, when present, retain their upstream metadata; their external runtime plugins are not included.
- Upstream hardware or revision distinctions beyond the source filename are not independently established.
- The URDF has no inertial element for `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`, `joint6_flange`.
