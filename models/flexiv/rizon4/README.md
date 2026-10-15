# Flexiv Rizon4

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Flexiv Rizon4 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Official manufacturer model files for the assembly identified below.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model | URDF | [`models/flexiv/rizon4/urdf/rizon4.urdf`](urdf/rizon4.urdf) | Local file loader; use a fixed base for mounted arms. |
| Robot model — Upstream robot assembly | MJCF | [`models/flexiv/rizon4/mjcf/menagerie/flexiv_rizon4.xml`](mjcf/menagerie/flexiv_rizon4.xml) | MuJoCo; complete relative resources are included. |
| Demonstration scene — Robot with floor, skybox and lighting | MJCF | [`models/flexiv/rizon4/mjcf/menagerie/scene.xml`](mjcf/menagerie/scene.xml) | MuJoCo; complete relative resources are included. |

## Mechanical information

The URDF information below describes its manufacturer or maintainer assembly. For the separate curated MJCF assembly, joint names and actuators, see [MJCF model notes](mjcf/README.md).

### Flexiv Rizon4

| Item | Definition |
|---|---|
| Hardware revision and gripper | Flexiv Rizon4; configuration represented by the entry. |
| Units | URDF SI conventions: metres, kilograms, radians. Mesh scaling is retained from upstream. |
| Base | `world`; attach this root frame to the consuming scene. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`, `joint7` (upstream declaration order; fixed joints omitted). |
| Gripper | No mimic coupling is declared. Any gripper joint limits remain in the entry. |
| End effector / TCP | Leaf frames: `flange`. Their upstream transforms are retained. |
| Included poses | No separate pose configuration is included. |

### URDF joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `joint1` | revolute | -2.8798 | 2.8798 | radians |
| `joint2` | revolute | -2.3562 | 2.3562 | radians |
| `joint3` | revolute | -3.0543 | 3.0543 | radians |
| `joint4` | revolute | -1.9548 | 2.7751 | radians |
| `joint5` | revolute | -3.0543 | 3.0543 | radians |
| `joint6` | revolute | -1.4835 | 4.6251 | radians |
| `joint7` | revolute | -3.0543 | 3.0543 | radians |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/flexiv/rizon4/urdf/rizon4.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/flexiv/rizon4/mjcf/menagerie/flexiv_rizon4.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF entry and referenced resources | [flexiv_description](https://github.com/flexivrobotics/flexiv_description) | `6d5145ea74bce2a7f61867a7ae3de3823ec6154f` | `urdf/flexiv.urdf.xacro` | [LICENSE](urdf/LICENSE), [NOTICES](urdf/NOTICES) |
| Curated MJCF and referenced assets | [Google DeepMind MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `flexiv_rizon4/` | [Model license](mjcf/menagerie/LICENSE), [notices](mjcf/menagerie/NOTICES) |

License: Apache-2.0. The license and attribution notices apply to the model entry and copied dependencies from the stated project.

## Model preparation

The MJCF entries and dependencies retain the curator’s model definitions and relative paths. [MJCF model notes](mjcf/README.md) describe that format separately.

 Xacro 2.1.1 expansion mappings: `{"arm_prefix": "", "arm_type": "", "arm_type_left": "", "arm_type_right": "", "dual_mounting_file": "/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi\u9879\u76ee\u5f00\u53d1/sources/robot-zoo-upstreams/flexiv_description/config/dual_robot_mounting.yaml", "external_axis_prefix": "", "gripper_name": "Flexiv-GN01", "gripper_name_left": "Flexiv-GN01", "gripper_name_right": "Flexiv-GN01", "inertia_parameters_file": "/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi\u9879\u76ee\u5f00\u53d1/sources/robot-zoo-upstreams/flexiv_description/config/Rizon4/inertia_parameters.yaml", "joint_limits_parameters_file": "/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi\u9879\u76ee\u5f00\u53d1/sources/robot-zoo-upstreams/flexiv_description/config/Rizon4/joint_limits.yaml", "kinematics_parameters_file": "", "kinematics_parameters_file_left": "", "kinematics_parameters_file_right": "", "load_gripper": "false", "load_gripper_left": "false", "load_gripper_right": "false", "load_mounted_ft_sensor": "false", "load_mounted_ft_sensor_left": "false", "load_mounted_ft_sensor_right": "false", "mounting_file": "/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi\u9879\u76ee\u5f00\u53d1/sources/robot-zoo-upstreams/flexiv_description/config/single_robot_mounting.yaml", "paired_mounting_file": "/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi\u9879\u76ee\u5f00\u53d1/sources/robot-zoo-upstreams/flexiv_description/config/dual_arm_mounting.yaml", "robot_sn": "", "robot_sn_left": "", "robot_sn_right": "", "robot_type": "Rizon4", "visual_parameters_file": "/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi\u9879\u76ee\u5f00\u53d1/sources/robot-zoo-upstreams/flexiv_description/config/Rizon4/visual_parameters.yaml"}`. Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/flexiv/rizon4/urdf/rizon4.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |
| `models/flexiv/rizon4/mjcf/menagerie/flexiv_rizon4.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/flexiv/rizon4/mjcf/menagerie/scene.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- ROS and Gazebo control extensions, when present, retain their upstream metadata; their external runtime plugins are not included.
- Upstream hardware or revision distinctions beyond the source filename are not independently established.
- The URDF has no inertial element for `world`, `base_link`, `link1`, `link2`, `link3`, `link4`, `link5`, `link6`, `link7`, `flange`.
