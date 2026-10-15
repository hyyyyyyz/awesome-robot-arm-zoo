# FANUC M710IC_50S

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="FANUC M710IC_50S model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

FANUC M710IC_50S, 6-joint robot body, with no gripper. The model is supplied by the manufacturer's GitHub organization for use as a robot description in an existing scene.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot body, no gripper | URDF | [`models/fanuc/m710ic_50s/urdf/m710ic_50s.urdf`](urdf/m710ic_50s.urdf) | Native URDF loader; resolve resources relative to the entry file; use a fixed base for dynamics. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | M710IC_50S; upstream robot body; no gripper or attached tool |
| Units | URDF: metres, kilograms, radians, seconds; mesh scale factors remain explicit in the entry |
| Base | `world`; `base_link` is attached by `base_joint` (xyz = `0 0 0` m, rpy = `0 0 0` rad) |
| Arm joint order | `J1` (revolute), `J2` (revolute), `J3` (revolute), `J4` (revolute), `J5` (revolute), `J6` (revolute) |
| Gripper | None |
| End effector / TCP | `ee_link`; `flange`; `fanuc_flange`. Fixed frame transforms: `J6_link` → `flange`: xyz = ` .175  0  0` m, rpy = `0 0 0` rad; `flange` → `fanuc_flange`: xyz = `0 0 0` m, rpy = `3.141592653589793 -1.5707963267948966 0.0` rad; `flange` → `ee_link`: xyz = `0 0 0` m, rpy = `0 0 0` rad |
| Included poses | No named poses are stored in this URDF. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/fanuc/m710ic_50s/urdf/m710ic_50s.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF definition and companion meshes | [FANUC-CORPORATION/fanuc_description](https://github.com/FANUC-CORPORATION/fanuc_description) — manufacturer-maintained | `fb40c9803a826ba68c7c8e28ba904a25efa7fcd2` | [`fanuc_m710_description/robot/m710ic_50s.urdf.xacro`](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_m710_description/robot/m710ic_50s.urdf.xacro); `fanuc_m710_description/meshes/` | [Apache-2.0](urdf/LICENSE) |
| Upstream package metadata | Same project | Same commit | `fanuc_m710_description/package.xml` | [Preserved manifest](urdf/source_package.xml) |

The package license declaration applies to the robot description and accompanying mesh resources. Upstream copyright and author notices are retained in the entry, package metadata and accompanying notice files. This collection preserves those source terms for the included files.

## Model preparation

Static URDF expanded from the upstream Xacro with xacro 2.1.1 using the upstream top-level defaults. Resource filenames resolve relative to the URDF file. The source mesh hierarchy is retained under `urdf/resources/`. Links, joint transforms, limits, mesh scales, inertial properties and collision definitions retain the upstream values.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/fanuc/m710ic_50s/urdf/m710ic_50s.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- Robot controllers, hardware drivers, calibrated tools and simulator-specific actuation are configured by the consuming project. Other simulator environments have not been tested.
