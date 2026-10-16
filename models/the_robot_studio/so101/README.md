# The Robot Studio SO-101

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="The Robot Studio SO-101 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

SO-101 follower in the upstream new-calibration convention, with virtual arm zeros at the middle of their ranges. A distinct leader URDF carries the handle and trigger assembly.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Follower robot model | URDF | [`models/the_robot_studio/so101/urdf/so101_new_calib.urdf`](urdf/so101_new_calib.urdf) | Native URDF loader; load visual and collision resources. Use the source fixed mounting convention. |
| Leader handle and trigger assembly | URDF | [`models/the_robot_studio/so101/urdf/leader/so101_leader_new_calib.urdf`](urdf/leader/so101_leader_new_calib.urdf) | Native URDF loader; load visual and collision resources. Use the source fixed mounting convention. |
| Follower robot model | MJCF | [`models/the_robot_studio/so101/mjcf/so101_new_calib.xml`](mjcf/so101_new_calib.xml) | MuJoCo native XML; retains source fixed-base, actuator and constraint definitions. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | SO-101 new-calibration follower; separate SO-101 leader with handle and trigger |
| Units | Metres, kilograms and radians; native mesh scales are retained. |
| Base | URDF `base_link`; MJCF `base` is fixed to the world. |
| Movable joint order | `shoulder_pan`, `shoulder_lift`, `elbow_flex`, `wrist_flex`, `wrist_roll`, `gripper` |
| Gripper | Follower `gripper`: −0.174533 to 1.74533 rad. Leader `gripper`: 0 to 0.785398 rad. Both are rotary joints with no mimic relationship. |
| End effector / TCP | Follower URDF `gripper_frame_link`; MJCF `gripperframe` site. Leader also provides `handle_frame_link`. |
| Included poses | No separate pose configuration is included. |

## Loading example

```python
from yourdfpy import URDF
robot = URDF.load('/absolute/path/to/awesome-robot-arm-zoo/models/the_robot_studio/so101/urdf/so101_new_calib.urdf',
                  load_meshes=True, load_collision_meshes=True,
                  build_collision_scene_graph=True)
robot.update_cfg({})

import mujoco
model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/the_robot_studio/so101/mjcf/so101_new_calib.xml')
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF entry and referenced meshes | [SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100) | `a758567c3978dfeefe282ede0500085a48fe8f78` | [`Simulation/SO101/so101_new_calib.urdf`](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.urdf) and referenced resources | [Apache-2.0](urdf/LICENSE); [upstream license](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/LICENSE) |
| URDF entry and referenced meshes | [SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100) | `a758567c3978dfeefe282ede0500085a48fe8f78` | [`Simulation/SO101/so101_leader_new_calib.urdf`](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_leader_new_calib.urdf) and referenced resources | [Apache-2.0](urdf/leader/LICENSE); [upstream license](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/LICENSE) |
| MJCF entry and referenced meshes | [SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100) | `a758567c3978dfeefe282ede0500085a48fe8f78` | [`Simulation/SO101/so101_new_calib.xml`](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml) and referenced resources | [Apache-2.0](mjcf/LICENSE); [upstream license](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/LICENSE) |

The upstream SO-101 documentation attributes STS3215 motor parameters to the Open Duck Mini project. The supplied model parameters and attribution are retained.

## Model preparation

The upstream URDF and its referenced meshes are packaged for standalone file loading. Relative resource paths are retained; XML formatting is normalized. Source joints, inertia, limits, mesh scales and collision definitions are retained. The native MJCF and referenced resources retain their upstream contents, including defaults, actuators and constraints. Only resources needed by the listed entries are included.

## Loading verification

| Entry | Environment and simulator version | Verification steps | Result |
|---|---|---|---|
| [`so101_new_calib.urdf`](urdf/so101_new_calib.urdf) | macOS; yourdfpy 0.0.60 | Copy the entire format directory, load from an unrelated working directory, configure movable joints, inspect visual and collision bounds. | Passed; 8 links, 6 actuated joints, 17 visual and 7 collision geometries. |
| [`so101_leader_new_calib.urdf`](urdf/leader/so101_leader_new_calib.urdf) | macOS; yourdfpy 0.0.60 | Copy the entire format directory, load from an unrelated working directory, configure movable joints, inspect visual and collision bounds. | Passed; 9 links, 6 actuated joints, 18 visual and 7 collision geometries. |
| [`so101_new_calib.xml`](mjcf/so101_new_calib.xml) | macOS; MuJoCo 3.16.0 | Copy the entire format directory, load from an unrelated working directory, create data and run `mj_forward`. | Passed; 8 bodies, 6 joints, 30 geometries. |

## Known limitations

The source leader trigger travel and printed-part inertia are provisional CAD estimates. The source angular gripper representation differs from LeRobot’s 0–100 gripper mapping. The leader has no upstream MJCF. Physical contact behavior and servo fidelity have not been validated. Loading records establish resource completeness and native kinematics; they do not establish task or policy performance.
