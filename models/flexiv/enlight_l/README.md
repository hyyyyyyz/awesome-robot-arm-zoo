# Flexiv Enlight-L

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Flexiv Enlight-L model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Official manufacturer model files for the assembly identified below.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model | URDF | [`models/flexiv/enlight_l/urdf/enlight_l.urdf`](urdf/enlight_l.urdf) | Local file loader; use a fixed base for mounted arms. |

## Mechanical information

### Flexiv Enlight-L

| Item | Definition |
|---|---|
| Hardware revision and gripper | Flexiv Enlight-L; configuration represented by the entry. |
| Units | URDF SI conventions: metres, kilograms, radians. Mesh scaling is retained from upstream. |
| Base | `world`; attach this root frame to the consuming scene. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`, `joint7` (upstream declaration order; fixed joints omitted). |
| Gripper | No mimic coupling is declared. Any gripper joint limits remain in the entry. |
| End effector / TCP | Leaf frames: `flange`. Their upstream transforms are retained. |
| Included poses | No separate pose configuration is included. |

### URDF joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `joint1` | revolute | -6.3705 | 6.3705 | radians |
| `joint2` | revolute | -2.1817 | 2.1817 | radians |
| `joint3` | revolute | -6.3705 | 6.3705 | radians |
| `joint4` | revolute | -2.1817 | 2.1817 | radians |
| `joint5` | revolute | -6.3705 | 6.3705 | radians |
| `joint6` | revolute | -2.1817 | 2.1817 | radians |
| `joint7` | revolute | -6.3705 | 6.3705 | radians |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/flexiv/enlight_l/urdf/enlight_l.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF entry and referenced resources | [flexiv_description](https://github.com/flexivrobotics/flexiv_description) | `6d5145ea74bce2a7f61867a7ae3de3823ec6154f` | `urdf/flexiv.urdf.xacro` | [LICENSE](urdf/LICENSE), [NOTICES](urdf/NOTICES) |

License: Apache-2.0. The license and attribution notices apply to the model entry and copied dependencies from the stated project.

## Model preparation

 Xacro 2.1.1 expansion mappings: `{"arm_prefix": "", "arm_type": "", "arm_type_left": "", "arm_type_right": "", "dual_mounting_file": "/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi\u9879\u76ee\u5f00\u53d1/sources/robot-zoo-upstreams/flexiv_description/config/dual_robot_mounting.yaml", "external_axis_prefix": "", "gripper_name": "Flexiv-GN01", "gripper_name_left": "Flexiv-GN01", "gripper_name_right": "Flexiv-GN01", "inertia_parameters_file": "/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi\u9879\u76ee\u5f00\u53d1/sources/robot-zoo-upstreams/flexiv_description/config/Enlight-L/inertia_parameters.yaml", "joint_limits_parameters_file": "/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi\u9879\u76ee\u5f00\u53d1/sources/robot-zoo-upstreams/flexiv_description/config/Enlight-L/joint_limits.yaml", "kinematics_parameters_file": "", "kinematics_parameters_file_left": "", "kinematics_parameters_file_right": "", "load_gripper": "false", "load_gripper_left": "false", "load_gripper_right": "false", "load_mounted_ft_sensor": "false", "load_mounted_ft_sensor_left": "false", "load_mounted_ft_sensor_right": "false", "mounting_file": "/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi\u9879\u76ee\u5f00\u53d1/sources/robot-zoo-upstreams/flexiv_description/config/single_robot_mounting.yaml", "paired_mounting_file": "/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi\u9879\u76ee\u5f00\u53d1/sources/robot-zoo-upstreams/flexiv_description/config/dual_arm_mounting.yaml", "robot_sn": "", "robot_sn_left": "", "robot_sn_right": "", "robot_type": "Enlight-L", "visual_parameters_file": "/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi\u9879\u76ee\u5f00\u53d1/sources/robot-zoo-upstreams/flexiv_description/config/Enlight-L/visual_parameters.yaml"}`. Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/flexiv/enlight_l/urdf/enlight_l.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- ROS and Gazebo control extensions, when present, retain their upstream metadata; their external runtime plugins are not included.
- Upstream hardware or revision distinctions beyond the source filename are not independently established.
- The URDF has no inertial element for `world`, `base_link`, `link1`, `link2`, `link3`, `link4`, `link5`, `link6`, `link7`, `flange`.
