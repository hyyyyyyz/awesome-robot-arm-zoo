# DENSO HSR065A1-N32-NNN-NNN A

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="DENSO HSR065A1-N32-NNN-NNN A model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

DENSO HSR065A1-N32-NNN-NNN A, 4-joint SCARA robot body, with no gripper. The model is supplied by the manufacturer's GitHub organization for use as a robot description in an existing scene.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Scara robot body, no gripper | URDF | [`models/denso/hsr065a1_n32/urdf/hsr065a1_n32.urdf`](urdf/hsr065a1_n32.urdf) | Native URDF loader; resolve resources relative to the entry file; use a fixed base for dynamics. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | HSR065A1-N32-NNN-NNN A; upstream SCARA robot body; no gripper or attached tool |
| Units | URDF: metres, kilograms, radians, seconds; mesh scale factors remain explicit in the entry |
| Base | `world`; `base_link` is attached by `joint_w` (xyz = `0 0 0` m, rpy = `0 0 0` rad) |
| Arm joint order | `joint_1` (revolute), `joint_2` (revolute), `joint_3` (prismatic), `joint_4` (revolute) |
| Gripper | None |
| End effector / TCP | Terminal link(s): `J4`; no separate calibrated TCP is specified |
| Included poses | No named poses are stored in this URDF. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/denso/hsr065a1_n32/urdf/hsr065a1_n32.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF definition and companion meshes | [DENSORobot/denso_robot_ros2](https://github.com/DENSORobot/denso_robot_ros2) — manufacturer-maintained | `2805694999b0375861e632426b5abc484d9a9936` | [`denso_robot_descriptions/urdf/denso_robot.urdf.xacro`](https://github.com/DENSORobot/denso_robot_ros2/blob/2805694999b0375861e632426b5abc484d9a9936/denso_robot_descriptions/urdf/denso_robot.urdf.xacro); `denso_robot_descriptions/robots/hsr065a1_n32/meshes/` | [Apache-2.0](urdf/LICENSE) |
| Upstream package metadata | Same project | Same commit | `denso_robot_descriptions/package.xml` | [Preserved manifest](urdf/source_package.xml) |

The package license declaration applies to the robot description and accompanying mesh resources. Upstream copyright and author notices are retained in the entry, package metadata and accompanying notice files. This collection preserves those source terms for the included files.

## Model preparation

Static URDF expanded from the upstream Xacro with xacro 2.1.1 using `model:=hsr065a1_n32`, `namespace:=`, `transmission_hw_interface:=`, `verbose:=false`, `sim:=false`, `ip_address:=192.168.0.1`, `send_format:=288`, `recv_format:=292`, `robot_name:=HSR065A1-N32-NNN-NNN A`, `robot_joints:=4`, `joint_1:=1`, `joint_2:=1`, `joint_3:=0`, `joint_4:=1`, `controller_type:=8`, `arm_group:=0`. Resource filenames resolve relative to the URDF file. The source mesh hierarchy is retained under `urdf/resources/`. Links, joint transforms, limits, mesh scales, inertial properties and collision definitions retain the upstream values. ROS 2 hardware-system and Gazebo control-plugin declarations are omitted from this standalone robot entry; upstream URDF transmission definitions are retained.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/denso/hsr065a1_n32/urdf/hsr065a1_n32.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- Upstream link masses are 1 kg with identity inertia tensors, and joint effort limits are 1; these are placeholder dynamics. The source README also identifies dummy speed/acceleration parameters in converted descriptions.
- Robot controllers, hardware drivers, calibrated tools and simulator-specific actuation are configured by the consuming project. Other simulator environments have not been tested.
