# Trossen Stationary AI

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Trossen Stationary AI model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Complete stationary bimanual assembly with two WXAI follower arms, parallel grippers, worktable, frame, two external cameras and two wrist cameras.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Complete dual WXAI worktable and camera assembly | MJCF | [`models/trossen/stationary_ai/mjcf/stationary_ai/stationary_ai.xml`](mjcf/stationary_ai/stationary_ai.xml) | MuJoCo native XML loader; use an absolute entry path. |
| Complete dual WXAI worktable and camera assembly | URDF | [`models/trossen/stationary_ai/urdf/stationary_ai.urdf`](urdf/stationary_ai.urdf) | Native URDF geometry loader; choose base attachment in the consuming simulator. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | Stationary AI; dual WXAI followers with D405 wrist cameras |
| Units | Metres, kilograms, radians; native mesh scales are retained. |
| Base | Fixed `tabletop_link`; arm joints use `follower_left_` and `follower_right_` prefixes. |
| Arm joint order | Per side: `joint_0`, `joint_1`, `joint_2`, `joint_3`, `joint_4`, `joint_5`, preceded by the corresponding follower prefix. |
| Gripper | Each side has `left_carriage_joint` (0–0.044 m) and a coupled `right_carriage_joint`, using URDF mimic and MJCF equality definitions. |
| End effector / TCP | URDF: `follower_left_ee_gripper_link`, `follower_right_ee_gripper_link`; MJCF: `follower_left_ee_site`, `follower_right_ee_site`. |
| Included poses | MJCF `home` keyframe; URDF supplies no separate pose configuration. |

## Loading example

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/trossen/stationary_ai/mjcf/stationary_ai/stationary_ai.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| MJCF and referenced resources | [Upstream project](https://github.com/TrossenRobotics/trossen_arm_mujoco) | `77aba5d32654f17945f139e63310e7a3ac2cd4ab` | `trossen_arm_mujoco/assets/stationary_ai` | [BSD-3-Clause](mjcf/LICENSE) |
| URDF and referenced resources | [Upstream project](https://github.com/TrossenRobotics/trossen_arm_description) | `d463e04e347e3eba016a80017b72cb78ee6b7ef8` | `urdf/generated/stationary_ai.urdf` | [BSD-3-Clause](urdf/LICENSE) |

Upstream copyright notices and redistribution terms are retained alongside each format.

## Model preparation

Generated manufacturer URDF files retain upstream links, meshes, inertia, limits and mimic definitions; package resource references are rewritten to local `meshes/` paths. Native MJCF retains the upstream dual-arm, table, frame and camera definitions, primitive collision approximations, gravity compensation and tuned actuators.

## Loading verification

Checks performed on 2026-10-16. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and simulator version | Verification steps | Result |
|---|---|---|---|
| `models/trossen/stationary_ai/mjcf/stationary_ai/stationary_ai.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Copy the complete format directory, change caller directory, compile XML and call `mj_forward`. | Passed, including resource relocation. |
| `models/trossen/stationary_ai/urdf/stationary_ai.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Copy the complete format directory, change caller directory, load visual/collision resources and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

The manufacturer MJCF camera fields of view and actuator settings are simulation approximations. Dynamics, camera calibration and hardware-controller equivalence have not been validated. URDF geometry loading does not run ROS control extensions.

Dynamic task execution, policy performance and training behavior have not been validated.
