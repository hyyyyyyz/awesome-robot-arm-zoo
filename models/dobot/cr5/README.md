# Dobot CR5

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Dobot CR5 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Official manufacturer model files for the assembly identified below.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model | URDF | [`models/dobot/cr5/urdf/cr5.urdf`](urdf/cr5.urdf) | Local file loader; use a fixed base for mounted arms. |

## Mechanical information

### Dobot CR5

| Item | Definition |
|---|---|
| Hardware revision and gripper | Dobot CR5; configuration represented by the entry. |
| Units | URDF SI conventions: metres, kilograms, radians. Mesh scaling is retained from upstream. |
| Base | `dummy_link`; attach this root frame to the consuming scene. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6` (upstream declaration order; fixed joints omitted). |
| Gripper | No mimic coupling is declared. Any gripper joint limits remain in the entry. |
| End effector / TCP | Leaf frames: `Link6`. Their upstream transforms are retained. |
| Included poses | No separate pose configuration is included. |

### URDF joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `joint1` | revolute | -6.28 | 6.28 | radians |
| `joint2` | revolute | -6.28 | 6.28 | radians |
| `joint3` | revolute | -2.793 | 2.793 | radians |
| `joint4` | revolute | -6.28 | 6.28 | radians |
| `joint5` | revolute | -6.28 | 6.28 | radians |
| `joint6` | revolute | -6.28 | 6.28 | radians |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/dobot/cr5/urdf/cr5.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF entry and referenced resources | [dobot_tcp_ip_ros](https://github.com/Dobot-Arm/TCP-IP-ROS-6AXis) | `0924e785f1827b7125ba4ba2bc3325811ed21c18` | `dobot_description/urdf/cr5_robot.urdf` | [LICENSE](urdf/LICENSE), [NOTICES](urdf/NOTICES) |

License: MIT. The license and attribution notices apply to the model entry and copied dependencies from the stated project.

## Model preparation

 Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/dobot/cr5/urdf/cr5.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- ROS and Gazebo control extensions, when present, retain their upstream metadata; their external runtime plugins are not included.
- Upstream hardware or revision distinctions beyond the source filename are not independently established.
- The URDF has no inertial element for `dummy_link`.
