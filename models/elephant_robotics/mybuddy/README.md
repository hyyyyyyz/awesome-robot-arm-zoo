# Elephant Robotics mybuddy

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Elephant Robotics mybuddy model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Official myBuddy dual-arm assembly with two six-axis arms and a rotating base.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Complete dual-arm assembly — arm | URDF | [`models/elephant_robotics/mybuddy/urdf/arm/mybuddy.urdf`](urdf/arm/mybuddy.urdf) | Local file loader; use a fixed base for mounted arms. |

## Mechanical information

### arm

| Item | Definition |
|---|---|
| Hardware revision and gripper | myBuddy dual-arm robot: two six-axis arms plus the revolving base. |
| Units | URDF SI conventions: metres, kilograms, radians. Mesh scaling is retained from upstream. |
| Base | `base`; attach this root frame to the consuming scene. |
| Movable joint order | `joint1_L`, `joint2_L`, `joint3_L`, `joint4_L`, `joint5_L`, `joint6_L`, `joint1_R`, `joint2_R`, `joint3_R`, `joint4_R`, `joint5_R`, `joint6_R`, `base_link1` (upstream declaration order; fixed joints omitted). |
| Gripper | No mimic coupling is declared. Any gripper joint limits remain in the entry. |
| End effector / TCP | Leaf frames: `link6_R`, `link6_L`. Their upstream transforms are retained. |
| Included poses | No separate pose configuration is included. |

### URDF / arm joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `joint1_L` | revolute | -2.8798 | 2.8798 | radians |
| `joint2_L` | revolute | -2.8798 | 2.8798 | radians |
| `joint3_L` | revolute | -2.8798 | 2.8798 | radians |
| `joint4_L` | revolute | -2.8798 | 2.8798 | radians |
| `joint5_L` | revolute | -2.8798 | 2.8798 | radians |
| `joint6_L` | revolute | -3.0543 | 3.0543 | radians |
| `joint1_R` | revolute | -2.8798 | 2.8798 | radians |
| `joint2_R` | revolute | -2.8798 | 2.8798 | radians |
| `joint3_R` | revolute | -2.8798 | 2.8798 | radians |
| `joint4_R` | revolute | -2.8798 | 2.8798 | radians |
| `joint5_R` | revolute | -2.8798 | 2.8798 | radians |
| `joint6_R` | revolute | -3.0543 | 3.0543 | radians |
| `base_link1` | revolute | -2.0943 | 2.0943 | radians |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/elephant_robotics/mybuddy/urdf/arm/mybuddy.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF / arm entry and referenced resources | [mycobot_ros](https://github.com/elephantrobotics/mycobot_ros) | `c0d6fbe8f7d9b18b46a9fcb0b041e5bc2d66196b` | `mycobot_description/urdf/mybuddy/mybuddy.urdf` | [LICENSE](urdf/arm/LICENSE), [NOTICES](urdf/arm/NOTICES) |

License: BSD-3-Clause. The license and attribution notices apply to the model entry and copied dependencies from the stated project.

## Model preparation

The upstream README identifies the repository license as BSD-3-Clause, copyright 2020–2023 Elephant Robotics. Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/elephant_robotics/mybuddy/urdf/arm/mybuddy.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Bundled COLLADA meshes declare length units in their asset metadata. The plain yourdfpy 0.0.60 / trimesh 5.1.1 loader does not apply those units; the preview renderer applies them to meshes and file-local transforms. Consuming loaders must honor the declared units. Recorded loading checks cover resource resolution and joint configuration updates, not dimensional accuracy.

Dynamic task execution, controller performance and training behavior have not been validated.

- ROS and Gazebo control extensions, when present, retain their upstream metadata; their external runtime plugins are not included.
- Upstream hardware or revision distinctions beyond the source filename are not independently established.
- The URDF has no inertial element for `base`, `link1`, `link1_R`, `link2_R`, `link3_R`, `link4_R`, `link5_R`, `link6_R`, `link1_L`, `link2_L`, `link3_L`, `link4_L`, `link5_L`, `link6_L`.
