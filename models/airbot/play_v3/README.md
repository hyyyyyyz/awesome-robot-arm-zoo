# AIRBOT Play v3

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="AIRBOT Play v3 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Six-axis AIRBOT Play with a two-finger parallel gripper and wrist camera, in the upstream table-and-floor demonstration scene. The source v3 gripper URDF identifies this Play revision and uses the same arm kinematic dimensions as the native MJCF.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Demonstration scene — Fixed-base Play v3 arm, gripper, table, floor and lighting | MJCF | [`models/airbot/play_v3/mjcf/source/manipulator/robot_airbot_play.xml`](mjcf/source/manipulator/robot_airbot_play.xml) | Native MuJoCo XML. Load by absolute path; base, furniture, floor and lighting follow the source entry. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | AIRBOT Play v3; native two-finger parallel gripper. |
| Units | Metres, kilograms and radians; slide and tendon coordinates use the source definitions below. |
| Base | `airbot_play_pose` fixes the arm at z = 0.78 m; `arm_base` is the robot base. The scene retains its table and floor. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`, `endleft`, `endright`. |
| Gripper | `endleft`: 0 to 0.04 m; `endright`: −0.04 to 0 m. The equality constraint enforces opposite displacement. The `gripper_gear` tendon is `0.5 × endleft − 0.5 × endright`; its position actuator accepts 0–0.04 m. |
| Actuation | Six joint position actuators and one tendon position actuator. Source gains and force limits are retained. |
| End effector / TCP | `endpoint` site on `link6`, with the source position and orientation; `armbase` is the base reference site. |
| Cameras and sensors | `eye_arm` camera; joint and endpoint sensor definitions are retained. |
| Included poses | `home` keyframe; reset with `mujoco.mj_resetDataKeyframe` when desired. |

## Loading example

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/airbot/play_v3/mjcf/source/manipulator/robot_airbot_play.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Native MJCF entry, included robot/scene/sensor files and referenced meshes | [DISCOVERSE](https://github.com/discoverse-dev/DISCOVERSE) | `d67f47c084aba0e0cf422a8725235f8b9238655a` | [`models/mjcf/manipulator/robot_airbot_play.xml`](https://github.com/discoverse-dev/DISCOVERSE/blob/d67f47c084aba0e0cf422a8725235f8b9238655a/models/mjcf/manipulator/robot_airbot_play.xml) and its resource closure | [MIT](mjcf/LICENSE); [attribution](mjcf/NOTICES); [upstream license](https://github.com/discoverse-dev/DISCOVERSE/blob/d67f47c084aba0e0cf422a8725235f8b9238655a/LICENSE) |

Copyright (c) 2025 Yufei Jia. The complete source MIT license and source attribution accompany the format directory. These are DISCOVERSE simulation definitions.

The [companion v3 URDF](https://github.com/discoverse-dev/DISCOVERSE/blob/d67f47c084aba0e0cf422a8725235f8b9238655a/models/urdf/airbot_play_v3_gripper_fixed.urdf) declares `airbot_play_v3_gripper`. Its arm dimensions match this MJCF: 0.1172 m shoulder height and 0.27009 / 0.29015 / 0.23645 m link offsets. The native MJCF retains its own source inertia, limits, collision definitions and gripper transmission.

## Model preparation

The native XML and referenced mesh contents retain their upstream definitions. The source `models/mjcf/` hierarchy is named `source/` within this format directory, and `models/meshes/` is retained as `meshes/`. This preserves all relative include and compiler resource paths while keeping the complete runtime closure inside `mjcf/`. Authored physical parameters, collision shapes, materials, cameras, sensors, actuators, tendons, equality constraints and the `home` keyframe are retained.

## Loading verification

| Entry | Environment and simulator version | Verification steps | Result |
|---|---|---|---|
| [`robot_airbot_play.xml`](mjcf/source/manipulator/robot_airbot_play.xml) | macOS; MuJoCo 3.16.0 | Copy the complete format directory into a temporary location, change to an unrelated working directory, compile the absolute entry, create `MjData` and run `mj_forward`. | Passed; 13 bodies, 8 joints and 30 geometries. |

## Known limitations

The native MJCF uses authored primitive collision approximations and source actuator gains. Contact fidelity, hardware calibration, sensor images, controllers and task performance have not been validated. The loading record establishes local resource completeness and native forward kinematics.
