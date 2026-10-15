# Kinova Gen3 6-DOF with Robotiq 2F-85

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Kinova Gen3 6-DOF with Robotiq 2F-85 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Single arm with gripper. Robotiq 2F-85 parallel gripper.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Single arm with gripper | URDF | [`models/kinova/gen3_6dof_robotiq_2f_85/urdf/gen3_6dof_robotiq_2f_85.urdf`](urdf/gen3_6dof_robotiq_2f_85.urdf) | Native URDF loaders; select a fixed base in the consuming simulator when required. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | Kinova Gen3 6-DOF with Robotiq 2F-85; Robotiq 2F-85 parallel gripper |
| Units | Metres, kilograms, radians; native mesh scales are retained. |
| Base | `base_link` |
| Movable joint order | `joint_1`, `joint_2`, `joint_3`, `joint_4`, `joint_5`, `joint_6`, `finger_joint`, `left_inner_knuckle_joint`, `left_inner_finger_joint`, `right_outer_knuckle_joint`, `right_inner_knuckle_joint`, `right_inner_finger_joint` |
| Gripper relationships | left_inner_knuckle_joint follows finger_joint; left_inner_finger_joint follows finger_joint; right_outer_knuckle_joint follows finger_joint; right_inner_knuckle_joint follows finger_joint; right_inner_finger_joint follows finger_joint |
| End effector / TCP | `end_effector_link`, `tool_frame` |
| Included poses | No separate pose configuration is included. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/kinova/gen3_6dof_robotiq_2f_85/urdf/gen3_6dof_robotiq_2f_85.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Kinova URDF and Kinova meshes | [Official manufacturer repository](https://github.com/Kinovarobotics/ros_kortex) | `c3280d8a6a6b5d96590d51538e3f265710a6c77d` | `kortex_description/robots/gen3_robotiq_2f_85.xacro` and referenced model resources | [Upstream terms](urdf/LICENSE) |
| Robotiq 2F-85 meshes | [Robotiq description distributed by Kinova](https://github.com/Kinovarobotics/ros_kortex) | `c3280d8a6a6b5d96590d51538e3f265710a6c77d` | `kortex_description/grippers/robotiq_2f_85/meshes/` | [Robotiq terms](urdf/licenses/kortex_description/grippers/robotiq_2f_85/LICENSE) |

Upstream copyright notices and redistribution terms are retained. Any independently licensed resource notices used by this assembly are preserved under `urdf/licenses/`.

## Model preparation

The static URDF retains the upstream links, joints, inertia, limits, collision shapes and mesh scales. Resource references resolve within the format directory. Xacro sources are expanded with xacro 2.1.1 where applicable. Source argument values: `{"arm": "gen3", "dof": "6", "gripper": "robotiq_2f_85", "prefix": "", "sim": "false", "vision": "true"}`. The MuJoCo-specific mesh-directory override, when present in the source, is omitted so that the prepared mesh paths are used.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/kinova/gen3_6dof_robotiq_2f_85/urdf/gen3_6dof_robotiq_2f_85.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

ROS/Gazebo extensions in the source model require the corresponding runtime if used; direct URDF geometry loading does not execute those plugins. The consuming project supplies its controller and task configuration.
