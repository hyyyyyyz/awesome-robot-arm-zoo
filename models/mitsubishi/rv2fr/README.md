# Mitsubishi Electric MELFA RV2FR

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Mitsubishi Electric MELFA RV2FR model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Mitsubishi Electric MELFA RV2FR, 6-joint robot body, with no gripper. The model is supplied by the manufacturer's GitHub organization for use as a robot description in an existing scene.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot body, no gripper | URDF | [`models/mitsubishi/rv2fr/urdf/rv2fr.urdf`](urdf/rv2fr.urdf) | Native URDF loader; resolve resources relative to the entry file; use a fixed base for dynamics. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | RV2FR; upstream robot body; no gripper or attached tool |
| Units | URDF: metres, kilograms, radians, seconds; mesh scale factors remain explicit in the entry |
| Base | `world`; `rv2fr_base` is attached by `rv2fr_world_to_base` (xyz = `0.0 0.0 0.0` m, rpy = `0 0 0` rad) |
| Arm joint order | `rv2fr_joint_1` (revolute), `rv2fr_joint_2` (revolute), `rv2fr_joint_3` (revolute), `rv2fr_joint_4` (revolute), `rv2fr_joint_5` (revolute), `rv2fr_joint_6` (revolute) |
| Gripper | None |
| End effector / TCP | `rv2fr_hand_flange`; `rv2fr_default_tcp`. Fixed frame transforms: `rv2fr_hand_flange` → `rv2fr_default_tcp`: xyz = `0.0 0.0 0.0` m, rpy = `0 0 0` rad |
| Included poses | No named poses are stored in this URDF. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/mitsubishi/rv2fr/urdf/rv2fr.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF definition and companion meshes | [MitsubishiElectric/melfa_ros2_driver](https://github.com/MitsubishiElectric/melfa_ros2_driver) — manufacturer-maintained | `10098bed6bcca4e4bef46e36389a839065f8cb22` | [`melfa_description/urdf/rv2fr/rv2fr.urdf`](https://github.com/MitsubishiElectric/melfa_ros2_driver/blob/10098bed6bcca4e4bef46e36389a839065f8cb22/melfa_description/urdf/rv2fr/rv2fr.urdf); `melfa_description/meshes/` | [Apache-2.0](urdf/LICENSE) |
| Upstream package metadata | Same project | Same commit | `melfa_description/package.xml` | [Preserved manifest](urdf/source_package.xml) |

The package license declaration applies to the robot description and accompanying mesh resources. Upstream copyright and author notices are retained in the entry, package metadata and accompanying notice files. This collection preserves those source terms for the included files.

## Model preparation

The upstream static URDF is retained with local resource filenames. Resource filenames resolve relative to the URDF file. The source mesh hierarchy is retained under `urdf/resources/`. Links, joint transforms, limits, mesh scales, inertial properties and collision definitions retain the upstream values.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/mitsubishi/rv2fr/urdf/rv2fr.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- The upstream model omits inertial definitions for 7 geometry-bearing link(s); dynamics engines may supply their own defaults.
- The upstream joint effort limits are 1. This entry carries the source kinematic description; actuator torque calibration is not supplied.
- Robot controllers, hardware drivers, calibrated tools and simulator-specific actuation are configured by the consuming project. Other simulator environments have not been tested.
