# Pollen Robotics Reachy 2021

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Pollen Robotics Reachy 2021 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Dual-arm upper body with head and pedestal. Native Reachy grippers.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Dual-arm upper body with head and pedestal | URDF | [`models/pollen_robotics/reachy_2021/urdf/reachy_2021.urdf`](urdf/reachy_2021.urdf) | Native URDF loaders; select a fixed base in the consuming simulator when required. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | Pollen Robotics Reachy 2021; Native Reachy grippers |
| Units | Metres, kilograms, radians; native mesh scales are retained. |
| Base | `pedestal` |
| Movable joint order | `r_antenna`, `l_antenna`, `r_shoulder_pitch`, `r_shoulder_roll`, `r_arm_yaw`, `r_elbow_pitch`, `r_forearm_yaw`, `r_wrist_pitch`, `r_wrist_roll`, `r_gripper`, `l_shoulder_pitch`, `l_shoulder_roll`, `l_arm_yaw`, `l_elbow_pitch`, `l_forearm_yaw`, `l_wrist_pitch`, `l_wrist_roll`, `l_gripper`, `neck_roll`, `neck_pitch`, `neck_yaw` |
| Gripper relationships | No URDF mimic relationships are declared. |
| End effector / TCP | Use the terminal link frames defined by the URDF; no additional TCP offset is introduced. |
| Included poses | No separate pose configuration is included. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/pollen_robotics/reachy_2021/urdf/reachy_2021.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF and its referenced resources | [Official manufacturer repository](https://github.com/pollen-robotics/reachy_description_ros2) | `aef3cb7a26802a34361b2ceb57ca6fbca9e8898c` | `urdf/reachy.URDF` and referenced model resources | [Upstream terms](urdf/LICENSE) |

Upstream copyright notices and redistribution terms are retained. Any independently licensed resource notices used by this assembly are preserved under `urdf/licenses/`.

## Model preparation

The static URDF retains the upstream links, joints, inertia, limits, collision shapes and mesh scales. Resource references resolve within the format directory. Xacro sources are expanded with xacro 2.1.1 where applicable. Source argument values: `{}`. The MuJoCo-specific mesh-directory override, when present in the source, is omitted so that the prepared mesh paths are used.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/pollen_robotics/reachy_2021/urdf/reachy_2021.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

ROS/Gazebo extensions in the source model require the corresponding runtime if used; direct URDF geometry loading does not execute those plugins. The consuming project supplies its controller and task configuration.
