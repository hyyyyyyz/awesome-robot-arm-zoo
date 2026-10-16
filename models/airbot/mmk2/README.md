# AIRBOT MMK2

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="AIRBOT MMK2 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Complete AIRBOT MMK2 mobile manipulator with a free chassis, two driven wheels, lift, pan/tilt head, two six-axis arms and two parallel grippers. The upstream entry includes its floor and lighting.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Demonstration scene — Complete MMK2 mobile manipulator with floor and lighting | MJCF | [`models/airbot/mmk2/mjcf/source/mmk2_floor.xml`](mjcf/source/mmk2_floor.xml) | Native MuJoCo XML. Load by absolute path; free base, floor and lighting follow the source entry. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | AIRBOT MMK2; native two-finger parallel grippers. |
| Units | Metres, kilograms and radians; slide and tendon coordinates use the source definitions below. |
| Base | `mmk2` body has an unnamed free joint. `agv_link` carries the chassis and the `base_link` reference site. |
| Movable joint order | Unnamed free-base joint, `lft_wheel_joint`, `rgt_wheel_joint`, `slide_joint`, `head_yaw_joint`, `head_pitch_joint`, `lft_arm_joint1`–`lft_arm_joint6`, `lft_finger_right_joint`, `lft_finger_left_joint`, `rgt_arm_joint1`–`rgt_arm_joint6`, `rgt_finger_right_joint`, `rgt_finger_left_joint`. |
| Gripper | Each side has two finger slides coupled with equal and opposite displacement. Its fixed tendon is `−12.5 × finger_left_joint + 12.5 × finger_right_joint`; the `lft_gripper` / `rgt_gripper` position controls use 0–1. |
| Actuation | Two wheel motors, lift and head position controls, six position controls per arm and one tendon control per gripper; 19 actuators total. |
| End effector / TCP | `lft_endpoint` and `rgt_endpoint` sites; `base_link` and `headeye` reference sites are retained. |
| Cameras and sensors | `head_cam`, `lft_handeye` and `rgt_handeye` cameras; `left_cam` / `right_cam` reference sites, joint sensors and base/endpoint sensors are retained. |
| Included poses | `home` keyframe; reset with `mujoco.mj_resetDataKeyframe` when desired. |

## Loading example

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/airbot/mmk2/mjcf/source/mmk2_floor.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Native MJCF entry, included robot/scene/sensor files and referenced meshes | [DISCOVERSE](https://github.com/discoverse-dev/DISCOVERSE) | `d67f47c084aba0e0cf422a8725235f8b9238655a` | [`models/mjcf/mmk2_floor.xml`](https://github.com/discoverse-dev/DISCOVERSE/blob/d67f47c084aba0e0cf422a8725235f8b9238655a/models/mjcf/mmk2_floor.xml) and its resource closure | [MIT](mjcf/LICENSE); [attribution](mjcf/NOTICES); [upstream license](https://github.com/discoverse-dev/DISCOVERSE/blob/d67f47c084aba0e0cf422a8725235f8b9238655a/LICENSE) |

Copyright (c) 2025 Yufei Jia. The complete source MIT license and source attribution accompany the format directory. These are DISCOVERSE simulation definitions.

The native `mmk2_floor.xml` and `mobile_chassis/mmk2/` components define the exact supplied assembly. The copied source includes the shared AIRBOT arm dependencies referenced by MMK2.

## Model preparation

The native XML and referenced mesh contents retain their upstream definitions. The source `models/mjcf/` hierarchy is named `source/` within this format directory, and `models/meshes/` is retained as `meshes/`. This preserves all relative include and compiler resource paths while keeping the complete runtime closure inside `mjcf/`. Authored physical parameters, collision shapes, materials, cameras, sensors, actuators, tendons, equality constraints and the `home` keyframe are retained.

## Loading verification

| Entry | Environment and simulator version | Verification steps | Result |
|---|---|---|---|
| [`mmk2_floor.xml`](mjcf/source/mmk2_floor.xml) | macOS; MuJoCo 3.16.0 | Copy the complete format directory into a temporary location, change to an unrelated working directory, compile the absolute entry, create `MjData` and run `mj_forward`. | Passed; 30 bodies, 22 joints and 73 geometries. |

## Known limitations

The chassis collision geometry includes source primitive approximations. Wheel-ground response, lift dynamics, sensor images, controllers and mobile-manipulation tasks have not been validated. The loading record establishes local resource completeness and native forward kinematics.
