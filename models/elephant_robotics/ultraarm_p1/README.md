# Elephant Robotics ultraarm p1

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Elephant Robotics ultraarm p1 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Official manufacturer model files for the assembly identified below.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model — arm | URDF | [`models/elephant_robotics/ultraarm_p1/urdf/arm/ultraarm_p1.urdf`](urdf/arm/ultraarm_p1.urdf) | Local file loader; use a fixed base for mounted arms. |

## Mechanical information

### arm

| Item | Definition |
|---|---|
| Hardware revision and gripper | Elephant Robotics ultraarm p1; configuration represented by the entry. |
| Units | URDF SI conventions: metres, kilograms, radians. Mesh scaling is retained from upstream. |
| Base | `world`; attach this root frame to the consuming scene. |
| Movable joint order | `J1`, `J2`, `center`, `CENTER_V_2`, `J3_4`, `J3`, `J3_5`, `J4`, `J2_2`, `center_v_1` (upstream declaration order; fixed joints omitted). |
| Gripper | center mimics J2 (multiplier -1, offset 0); CENTER_V_2 mimics J3 (multiplier 1, offset 0); J3_4 mimics J3 (multiplier -1, offset 0); J3_5 mimics J3 (multiplier -1, offset 0); J2_2 mimics J2 (multiplier 1, offset 0); center_v_1 mimics J2 (multiplier -1, offset 0) |
| End effector / TCP | Leaf frames: `J3_4_Link`, `J4_Link`, `FIX2_Link`, `fix1_Link`, `center_v_1_Link`. Their upstream transforms are retained. |
| Included poses | No separate pose configuration is included. |

### URDF / arm joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `J1` | revolute | -2.87 | 2.87 | radians |
| `J2` | revolute | -0.31 | 1.48 | radians |
| `center` | revolute | -1.48 | 0.31 | radians |
| `CENTER_V_2` | revolute | -0.017 | 1.91 | radians |
| `J3_4` | revolute | -1.91 | 0.017 | radians |
| `J3` | revolute | -0.017 | 1.91 | radians |
| `J3_5` | revolute | -1.91 | 0.017 | radians |
| `J4` | revolute | -3.12 | 3.12 | radians |
| `J2_2` | revolute | -0.31 | 1.48 | radians |
| `center_v_1` | revolute | -1.48 | 0.31 | radians |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/elephant_robotics/ultraarm_p1/urdf/arm/ultraarm_p1.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF / arm entry and referenced resources | [mycobot_ros](https://github.com/elephantrobotics/mycobot_ros) | `c0d6fbe8f7d9b18b46a9fcb0b041e5bc2d66196b` | `mycobot_description/urdf/ultraArm_p1/ultraArm_p1.urdf` | [LICENSE](urdf/arm/LICENSE), [NOTICES](urdf/arm/NOTICES) |

License: BSD-3-Clause. The license and attribution notices apply to the model entry and copied dependencies from the stated project.

## Model preparation

The upstream README identifies the repository license as BSD-3-Clause, copyright 2020–2023 Elephant Robotics. Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/elephant_robotics/ultraarm_p1/urdf/arm/ultraarm_p1.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- ROS and Gazebo control extensions, when present, retain their upstream metadata; their external runtime plugins are not included.
- Upstream hardware or revision distinctions beyond the source filename are not independently established.
- The URDF has no inertial element for `world`.
