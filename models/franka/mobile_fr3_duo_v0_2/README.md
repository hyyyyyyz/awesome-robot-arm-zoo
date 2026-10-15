# Franka Robotics MOBILE FR3 DUO V0 2

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Franka Robotics MOBILE FR3 DUO V0 2 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Mobile FR3 Duo v0.2, two FR3 v2.1 7-joint arms with two Franka Hands and the TMR v0.2 mobile base. The entry preserves the upstream kinematic, visual, collision, inertial and joint-limit definitions.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Complete assembly: Mobile FR3 Duo v0.2, two FR3 v2.1 7-joint arms with two Franka Hands and the TMR v0.2 mobile base | URDF | [`models/franka/mobile_fr3_duo_v0_2/urdf/mobile_fr3_duo_v0_2.urdf`](urdf/mobile_fr3_duo_v0_2.urdf) | A native URDF loader with relative mesh resolution; choose the mobile base attachment in the consuming scene. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | Mobile FR3 Duo v0.2, two FR3 v2.1 7-joint arms with two Franka Hands and the TMR v0.2 mobile base |
| Units | Metres, kilograms, radians; revolute joint effort in N·m and prismatic effort in N. Mesh scale attributes remain as supplied upstream. |
| Base | `base_link`; root of the URDF tree. Any supplied fixed base transform is retained. |
| Arm joint order | Left: `left_fr3v2_1_joint1` → `left_fr3v2_1_joint2` → `left_fr3v2_1_joint3` → `left_fr3v2_1_joint4` → `left_fr3v2_1_joint5` → `left_fr3v2_1_joint6` → `left_fr3v2_1_joint7`; right: `right_fr3v2_1_joint1` → `right_fr3v2_1_joint2` → `right_fr3v2_1_joint3` → `right_fr3v2_1_joint4` → `right_fr3v2_1_joint5` → `right_fr3v2_1_joint6` → `right_fr3v2_1_joint7`. |
| Mobile base and lift joints | `caster_front_left_steering_joint`, `caster_front_left_joint`, `tmrv0_2_joint_0`, `tmrv0_2_joint_1`, `rocker_arm_joint`, `caster_rear_right_steering_joint`, `caster_rear_right_joint`, `tmrv0_2_joint_2`, `tmrv0_2_joint_3`, `franka_spine_vertical_joint`; `franka_spine_vertical_joint` is the prismatic lift. |
| Gripper | `left_fr3v2_1_finger_joint1`: 0.0 to 0.04 m; `left_fr3v2_1_finger_joint2`: 0.0 to 0.04 m; mimics `left_fr3v2_1_finger_joint1` (multiplier 1, offset 0); `right_fr3v2_1_finger_joint1`: 0.0 to 0.04 m; `right_fr3v2_1_finger_joint2`: 0.0 to 0.04 m; mimics `right_fr3v2_1_finger_joint1` (multiplier 1, offset 0) |
| End effector / TCP | `left_fr3v2_1_link8`, `left_fr3v2_1_hand_tcp`, `right_fr3v2_1_link8`, `right_fr3v2_1_hand_tcp`; fixed transforms remain in the entry. |
| Included poses | No named poses are defined by this URDF entry. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/franka/mobile_fr3_duo_v0_2/urdf/mobile_fr3_duo_v0_2.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Static URDF and its bundled resources (franka_description) | [https://github.com/frankarobotics/franka_description](https://github.com/frankarobotics/franka_description) | `7aeeddc449edf8d62b594f9e36a81da53e7796f9` | `robots/mobile_fr3_duo_v0_2/mobile_fr3_duo_v0_2.urdf.xacro`; model mesh paths under the named packages | [LICENSE](urdf/LICENSE), [NOTICE](urdf/NOTICE) |

Bundled upstream resource directories: `meshes/accessories/fr3_duo_mount_v0_3/collision`, `meshes/accessories/fr3_duo_mount_v0_3/visual`, `meshes/accessories/franka_head_v0_2/collision`, `meshes/accessories/franka_head_v0_2/visual`, `meshes/accessories/franka_spine_v0_1/collision`, `meshes/accessories/franka_spine_v0_1/visual`, `meshes/robot_ee/franka_hand_white/collision`, `meshes/robot_ee/franka_hand_white/visual`, `meshes/robots/fr3v2_1/collision`, `meshes/robots/fr3v2_1/visual`, `meshes/robots/tmrv0_2/collision`, `meshes/robots/tmrv0_2/visual`.

License scope: Apache-2.0 for robot definitions, meshes and Franka Hand; copyright Franka Robotics GmbH, with the upstream NOTICE retained. The complete upstream license texts and notices accompany this format directory.

## Model preparation

The static entry was expanded with xacro 2.1.1 using with_sc:=False, ee_id:=franka_hand, hand:=True, no_prefix:=false, robot_type:=mobile_fr3_duo_v0_2. Resources were copied only when referenced by the entry or by one of its mesh/material files. Resource references are local relative paths. Mesh contents and physical parameters retain the upstream definitions. Expansion uses the upstream scripts/create_urdf.py convert_xacro_to_urdf function. The standard fine collision meshes are retained; with_sc is false, matching the official generator default.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/franka/mobile_fr3_duo_v0_2/urdf/mobile_fr3_duo_v0_2.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Bundled COLLADA meshes declare length units in their asset metadata. The plain yourdfpy 0.0.60 / trimesh 5.1.1 loader does not apply those units; the preview renderer applies them to meshes and file-local transforms. Consuming loaders must honor the declared units. Recorded loading checks cover resource resolution and joint configuration updates, not dimensional accuracy.

Dynamic task execution, controller performance and training behavior have not been validated.

ROS, Gazebo and physics simulators have not been verified for this entry.
