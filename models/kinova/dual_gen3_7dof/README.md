# Kinova dual Gen3 7-DOF

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Kinova dual Gen3 7-DOF model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Upstream dual-arm example. Two bare-flange Gen3 arms, upstream mounts at x = -1 and +1 metres.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Upstream dual-arm example | URDF | [`models/kinova/dual_gen3_7dof/urdf/dual_gen3_7dof.urdf`](urdf/dual_gen3_7dof.urdf) | Native URDF loaders; select a fixed base in the consuming simulator when required. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | Kinova dual Gen3 7-DOF; Two bare-flange Gen3 arms, upstream mounts at x = -1 and +1 metres |
| Units | Metres, kilograms, radians; native mesh scales are retained. |
| Base | `world` |
| Movable joint order | `left_joint_1`, `left_joint_2`, `left_joint_3`, `left_joint_4`, `left_joint_5`, `left_joint_6`, `left_joint_7`, `right_joint_1`, `right_joint_2`, `right_joint_3`, `right_joint_4`, `right_joint_5`, `right_joint_6`, `right_joint_7` |
| Gripper relationships | No URDF mimic relationships are declared. |
| End effector / TCP | `left_end_effector_link`, `left_tool_frame`, `right_end_effector_link`, `right_tool_frame` |
| Included poses | No separate pose configuration is included. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/kinova/dual_gen3_7dof/urdf/dual_gen3_7dof.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF and its referenced resources | [Official manufacturer repository](https://github.com/Kinovarobotics/ros_kortex) | `c3280d8a6a6b5d96590d51538e3f265710a6c77d` | `kortex_description/multiple_robots/kortex_dual_robots.xacro` and referenced model resources | [Upstream terms](urdf/LICENSE) |

Upstream copyright notices and redistribution terms are retained. Any independently licensed resource notices used by this assembly are preserved under `urdf/licenses/`.

## Model preparation

The static URDF retains the upstream links, joints, inertia, limits, collision shapes and mesh scales. Resource references resolve within the format directory. Xacro sources are expanded with xacro 2.1.1 where applicable. Source argument values: `{"left_arm": "gen3", "left_dof": "7", "left_gripper": "", "left_prefix": "left_", "left_sim": "false", "left_vision": "true", "right_arm": "gen3", "right_dof": "7", "right_gripper": "", "right_prefix": "right_", "right_sim": "false", "right_vision": "true"}`. The MuJoCo-specific mesh-directory override, when present in the source, is omitted so that the prepared mesh paths are used.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/kinova/dual_gen3_7dof/urdf/dual_gen3_7dof.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

ROS/Gazebo extensions in the source model require the corresponding runtime if used; direct URDF geometry loading does not execute those plugins. The consuming project supplies its controller and task configuration.
