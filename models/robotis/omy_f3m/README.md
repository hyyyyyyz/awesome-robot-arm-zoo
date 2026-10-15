# ROBOTIS OMY F3M

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="ROBOTIS OMY F3M model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Single arm with gripper and camera. ROBOTIS RH-P12-RN gripper and RealSense D405.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Single arm with gripper and camera | URDF | [`models/robotis/omy_f3m/urdf/omy_f3m.urdf`](urdf/omy_f3m.urdf) | Native URDF loaders; select a fixed base in the consuming simulator when required. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | ROBOTIS OMY F3M; ROBOTIS RH-P12-RN gripper and RealSense D405 |
| Units | Metres, kilograms, radians; native mesh scales are retained. |
| Base | `world` |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`, `rh_r1_joint`, `rh_r2`, `rh_l1`, `rh_l2` |
| Gripper relationships | rh_r2 follows rh_r1_joint; rh_l1 follows rh_r1_joint; rh_l2 follows rh_r1_joint |
| End effector / TCP | `end_effector_link`, `end_effector_flange_link` |
| Included poses | No separate pose configuration is included. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/robotis/omy_f3m/urdf/omy_f3m.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| ROBOTIS URDF and ROBOTIS meshes | [Official manufacturer repository](https://github.com/ROBOTIS-GIT/open_manipulator) | `d31000d90c679af9c982e73de8b12d777c5ff7dd` | `open_manipulator_description/urdf/omy_f3m/omy_f3m.urdf` and referenced model resources | [Upstream terms](urdf/LICENSE) |

RealSense D405 mesh: [official RealSense ROS repository](https://github.com/IntelRealSense/realsense-ros), commit `7a87097c499e3b0b69518d54a8e7a9ac1924e87c`, `realsense2_description/meshes/d405.stl`, covered by [Apache-2.0](urdf/LICENSE.realsense).

Upstream copyright notices and redistribution terms are retained. Any independently licensed resource notices used by this assembly are preserved under `urdf/licenses/`.

## Model preparation

The static URDF retains the upstream links, joints, inertia, limits, collision shapes and mesh scales. Resource references resolve within the format directory. Xacro sources are expanded with xacro 2.1.1 where applicable. Source argument values: `{}`. The MuJoCo-specific mesh-directory override, when present in the source, is omitted so that the prepared mesh paths are used.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/robotis/omy_f3m/urdf/omy_f3m.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

ROS/Gazebo extensions in the source model require the corresponding runtime if used; direct URDF geometry loading does not execute those plugins. The consuming project supplies its controller and task configuration.
