# Koch v1.1 follower

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Koch v1.1 follower model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Koch v1.1 follower arm with five arm joints and a rotary jaw gripper. This community MJCF is explicitly adapted to the v1.1 hardware and is distributed from the author’s Menagerie contribution branch.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Follower robot model | MJCF | [`models/koch/koch_v1_1/mjcf/low_cost_robot_arm.xml`](mjcf/low_cost_robot_arm.xml) | MuJoCo native XML; retains source fixed-base, actuator and constraint definitions. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | Koch v1.1 follower; XL430/XL330 servo assembly and rotary jaw |
| Units | Metres, kilograms and radians; native mesh scales are retained. |
| Base | `base_link`, fixed to the world. |
| Movable joint order | `base_rotation`, `pitch`, `elbow`, `wrist_pitch`, `wrist_roll`, `gripper` |
| Gripper | `gripper`: revolute, −1.60 to 0.032 rad, driving the moving jaw; no mimic or equality constraint is declared. |
| End effector / TCP | `gripper_static_finger` and `gripper_moving_finger` bodies; no separately calibrated TCP. |
| Included poses | `home` keyframe from the upstream MJCF. |

## Loading example

```python
import mujoco
model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/koch/koch_v1_1/mjcf/low_cost_robot_arm.xml')
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| MJCF entry and referenced meshes | [koch-v1-1-menagerie](https://github.com/s1lent4gnt/mujoco_menagerie) | `a8fa53ac6c8b422c698a2e03b89524138ed066cf` | [`low_cost_robot_arm/low_cost_robot_arm.xml`](https://github.com/s1lent4gnt/mujoco_menagerie/blob/a8fa53ac6c8b422c698a2e03b89524138ed066cf/low_cost_robot_arm/low_cost_robot_arm.xml) and referenced resources | [Apache-2.0](mjcf/LICENSE); [upstream license](https://github.com/s1lent4gnt/mujoco_menagerie/blob/a8fa53ac6c8b422c698a2e03b89524138ed066cf/low_cost_robot_arm/LICENSE) |

The model credits Alexander Koch’s original robot and the Hugging Face LeRobot team / Jess Moss v1.1 hardware adaptations. The v1.1 MJCF and meshes use the component Apache-2.0 license. The [component model notes](https://github.com/s1lent4gnt/mujoco_menagerie/blob/a8fa53ac6c8b422c698a2e03b89524138ed066cf/low_cost_robot_arm/README.md) identify the hardware revision and preparation.

## Model preparation

The native MJCF and referenced resources retain their upstream contents, including defaults, actuators and constraints. Only resources needed by the listed entries are included.

## Loading verification

| Entry | Environment and simulator version | Verification steps | Result |
|---|---|---|---|
| [`low_cost_robot_arm.xml`](mjcf/low_cost_robot_arm.xml) | macOS; MuJoCo 3.16.0 | Copy the entire format directory, load from an unrelated working directory, create data and run `mj_forward`. | Passed; 8 bodies, 6 joints, 26 geometries. |

## Known limitations

The source author describes the joint limits as approximate and uses manually prepared convex gripper collision meshes and fingertip pads. Physical dynamics, servo calibration and task performance have not been validated. Loading records establish resource completeness and native kinematics; they do not establish task or policy performance.
