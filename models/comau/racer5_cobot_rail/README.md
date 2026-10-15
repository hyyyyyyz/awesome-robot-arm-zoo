# Comau RACER5 COBOT RAIL

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Comau RACER5 COBOT RAIL model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Racer5 Cobot 6-joint arm on the upstream linear rail, without a gripper. The entry preserves the upstream kinematic, visual, collision, inertial and joint-limit definitions.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Complete assembly: Racer5 Cobot 6-joint arm on the upstream linear rail, without a gripper | URDF | [`models/comau/racer5_cobot_rail/urdf/racer5_cobot_rail.urdf`](urdf/racer5_cobot_rail.urdf) | A native URDF loader with relative mesh resolution; attach the base to the consuming scene. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | Racer5 Cobot 6-joint arm on the upstream linear rail, without a gripper |
| Units | Metres, kilograms, radians; revolute joint effort in N·m and prismatic effort in N. Mesh scale attributes remain as supplied upstream. |
| Base | `world`; root of the URDF tree. Any supplied fixed base transform is retained. |
| Arm joint order | `joint_1` → `joint_2` → `joint_3` → `joint_4` → `joint_5` → `joint_6` |
| External axis | `joint_7` is prismatic, -0.0 to 2.0 m. |
| Gripper | No gripper is included. |
| End effector / TCP | `world`; fixed transforms remain in the entry. |
| Included poses | No named poses are defined by this URDF entry. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/comau/racer5_cobot_rail/urdf/racer5_cobot_rail.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Static URDF and its bundled resources (racer5-cobot-rail_description) | [https://github.com/Comau/COMAU-ROS2-DRIVER](https://github.com/Comau/COMAU-ROS2-DRIVER) | `13af064b7a2b9fc1db3b24fb1d514850903e84cb` | `comau_ros2_client/comau_description/racer5-cobot-rail_description/robots/racer5-cobot-rail_robot.urdf.xacro`; model mesh paths under the named packages | [LICENSE](urdf/LICENSE) |

Bundled upstream resource directories: `racer5-cobot-rail_description/meshes/racer5-cobot`.

License scope: The repository LICENSE grants MIT terms, copyright 2025 Comau. The included [`package.xml`](urdf/package.xml) additionally declares BSD-2-Clause. The complete upstream license texts and notices accompany this format directory.

## Model preparation

The static entry was expanded with xacro 2.1.1 using upstream defaults. Resources were copied only when referenced by the entry or by one of its mesh/material files. Resource references are local relative paths. Mesh contents and physical parameters retain the upstream definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/comau/racer5_cobot_rail/urdf/racer5_cobot_rail.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

ROS, Gazebo and physics simulators have not been verified for this entry. The source package declares BSD-2-Clause while the repository-level license is MIT; both declarations are preserved. Controller integrations have not been tested.
