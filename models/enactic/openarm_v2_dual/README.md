# Enactic OpenArm v2 dual

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Enactic OpenArm v2 dual model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

OpenArm v2 bimanual assembly with seven joints per arm and two native pinch grippers. The URDF uses the default bimanual preset; the MJCF is the author-maintained v2 bimanual model.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Bimanual robot model | URDF | [`models/enactic/openarm_v2_dual/urdf/openarm_v20.urdf`](urdf/openarm_v20.urdf) | Native URDF loader; load visual and collision resources. Use the source fixed mounting convention. |
| Bimanual robot model | MJCF | [`models/enactic/openarm_v2_dual/mjcf/openarm_bimanual.xml`](mjcf/openarm_bimanual.xml) | MuJoCo native XML; retains source fixed-base, actuator and constraint definitions. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | OpenArm v2 default bimanual preset; left and right pinch grippers |
| Units | Metres, kilograms and radians; native mesh scales are retained. |
| Base | URDF `world`; MJCF fixes `openarm_left_base_link` and `openarm_right_base_link` at the upstream assembly transforms. |
| Movable joint order | `openarm_left_joint1`, `openarm_left_joint2`, `openarm_left_joint3`, `openarm_left_joint4`, `openarm_left_joint5`, `openarm_left_joint6`, `openarm_left_joint7`, `openarm_left_finger_joint1`, `openarm_left_finger_joint2`, `openarm_right_joint1`, `openarm_right_joint2`, `openarm_right_joint3`, `openarm_right_joint4`, `openarm_right_joint5`, `openarm_right_joint6`, `openarm_right_joint7`, `openarm_right_finger_joint1`, `openarm_right_finger_joint2` |
| Gripper | URDF finger joint 2 mimics joint 1 with multiplier 1 and offset 0 on each side. Left joint 1 range: 0 to 0.7854 rad; right: −0.7854 to 0 rad. MJCF preserves both equality constraints and position actuators. |
| End effector / TCP | URDF gripper bases `openarm_left_ee_base_link` / `openarm_right_ee_base_link`; MJCF sites `left_ee_control_point` / `right_ee_control_point`. |
| Included poses | No separate pose configuration is included. |

## Loading example

```python
from yourdfpy import URDF
robot = URDF.load('/absolute/path/to/awesome-robot-arm-zoo/models/enactic/openarm_v2_dual/urdf/openarm_v20.urdf',
                  load_meshes=True, load_collision_meshes=True,
                  build_collision_scene_graph=True)
robot.update_cfg({})

import mujoco
model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/enactic/openarm_v2_dual/mjcf/openarm_bimanual.xml')
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF entry and referenced meshes | [openarm_description](https://github.com/enactic/openarm_description) | `206eb8a4cf2e5e564536b4f5366ef369843a4aa7` | [`assets/robot/openarm_v2.0/urdf/openarm_v20.urdf.xacro`](https://github.com/enactic/openarm_description/blob/206eb8a4cf2e5e564536b4f5366ef369843a4aa7/assets/robot/openarm_v2.0/urdf/openarm_v20.urdf.xacro) and referenced resources | [Apache-2.0](urdf/LICENSE); [upstream license](https://github.com/enactic/openarm_description/blob/206eb8a4cf2e5e564536b4f5366ef369843a4aa7/LICENSE.txt) |
| MJCF entry and referenced meshes | [openarm_mujoco](https://github.com/enactic/openarm_mujoco) | `f017e1c8b0a35367fc673937f2f896ee473ac2cf` | [`v2/openarm_bimanual.xml`](https://github.com/enactic/openarm_mujoco/blob/f017e1c8b0a35367fc673937f2f896ee473ac2cf/v2/openarm_bimanual.xml) and referenced resources | [Apache-2.0](mjcf/LICENSE); [upstream license](https://github.com/enactic/openarm_mujoco/blob/f017e1c8b0a35367fc673937f2f896ee473ac2cf/LICENSE) |

Copyright 2025–2026 Enactic, Inc. Upstream copyright and Apache-2.0 terms are retained.

## Model preparation

The static URDF expands the upstream Xacro with xacro 2.1.1 and `robot_preset=default_bimanual`, `collapse_internal_empty_links=true`, `emit_grasp_frame=false`. Package resource paths are localized within `urdf/`. Source links, joints, inertia, mesh scales, limits and gripper mimic definitions are retained. The native MJCF and referenced resources retain their upstream contents, including defaults, actuators and constraints. Only resources needed by the listed entries are included.

## Loading verification

| Entry | Environment and simulator version | Verification steps | Result |
|---|---|---|---|
| [`openarm_v20.urdf`](urdf/openarm_v20.urdf) | macOS; yourdfpy 0.0.60 | Copy the entire format directory, load from an unrelated working directory, configure movable joints, inspect visual and collision bounds. | Passed; 22 links, 16 actuated joints, 65 visual and 21 collision geometries. |
| [`openarm_bimanual.xml`](mjcf/openarm_bimanual.xml) | macOS; MuJoCo 3.16.0 | Copy the entire format directory, load from an unrelated working directory, create data and run `mj_forward`. | Passed; 21 bodies, 18 joints, 94 geometries. |

## Known limitations

URDF and MJCF are independently maintained upstream descriptions; their collision and control definitions remain format-specific. ROS 2 control execution, physical contact fidelity and task policies have not been validated. Loading records establish resource completeness and native kinematics; they do not establish task or policy performance.
