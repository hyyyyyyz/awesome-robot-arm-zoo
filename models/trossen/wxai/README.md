# Trossen WXAI

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Trossen WXAI model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Native WXAI single-arm models with the parallel gripper. The base configuration omits the wrist camera; the follower configuration includes the Intel RealSense D405 and its mount.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Single WXAI arm without wrist camera | MJCF | [`models/trossen/wxai/mjcf/wxai/wxai_base.xml`](mjcf/wxai/wxai_base.xml) | MuJoCo native XML loader; use an absolute entry path. |
| Single WXAI arm with wrist camera | MJCF | [`models/trossen/wxai/mjcf/wxai/wxai_follower.xml`](mjcf/wxai/wxai_follower.xml) | MuJoCo native XML loader; use an absolute entry path. |
| Single WXAI arm without wrist camera | URDF | [`models/trossen/wxai/urdf/wxai_base.urdf`](urdf/wxai_base.urdf) | Native URDF geometry loader; choose base attachment in the consuming simulator. |
| Single WXAI arm with wrist camera | URDF | [`models/trossen/wxai/urdf/wxai_follower.urdf`](urdf/wxai_follower.urdf) | Native URDF geometry loader; choose base attachment in the consuming simulator. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | WXAI base and follower; native parallel gripper |
| Units | Metres, kilograms, radians; native mesh scales are retained. |
| Base | Fixed `base_link`. |
| Arm joint order | `joint_0`, `joint_1`, `joint_2`, `joint_3`, `joint_4`, `joint_5`. |
| Gripper | `left_carriage_joint` ranges from 0 to 0.044 m; `right_carriage_joint` follows it through URDF mimic or MJCF equality coupling. |
| End effector / TCP | URDF: `ee_gripper_link`; MJCF: `ee_site` at the gripper tip. |
| Included poses | MJCF `home` keyframe; URDF supplies no separate pose configuration. |

## Loading example

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/trossen/wxai/mjcf/wxai/wxai_base.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| MJCF and referenced resources | [Upstream project](https://github.com/TrossenRobotics/trossen_arm_mujoco) | `77aba5d32654f17945f139e63310e7a3ac2cd4ab` | `trossen_arm_mujoco/assets/wxai` | [BSD-3-Clause](mjcf/LICENSE) |
| URDF and referenced resources | [Upstream project](https://github.com/TrossenRobotics/trossen_arm_description) | `d463e04e347e3eba016a80017b72cb78ee6b7ef8` | `urdf/generated/wxai` | [BSD-3-Clause](urdf/LICENSE) |

Upstream copyright notices and redistribution terms are retained alongside each format.

## Model preparation

Generated manufacturer URDF files retain upstream geometry, inertial properties, limits and mimic relationships; package resource references are rewritten to local `meshes/` paths. Native MJCF files and their referenced mesh resources retain upstream contents. The manufacturer MJCF includes gravity compensation, simplified collision shapes and tuned position actuators.

## Loading verification

Checks performed on 2026-10-16. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and simulator version | Verification steps | Result |
|---|---|---|---|
| `models/trossen/wxai/mjcf/wxai/wxai_base.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Copy the complete format directory, change caller directory, compile XML and call `mj_forward`. | Passed, including resource relocation. |
| `models/trossen/wxai/mjcf/wxai/wxai_follower.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Copy the complete format directory, change caller directory, compile XML and call `mj_forward`. | Passed, including resource relocation. |
| `models/trossen/wxai/urdf/wxai_base.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Copy the complete format directory, change caller directory, load visual/collision resources and update the joint configuration. | Passed, including resource relocation. |
| `models/trossen/wxai/urdf/wxai_follower.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Copy the complete format directory, change caller directory, load visual/collision resources and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

MJCF controller gains, armature and friction parameters are the upstream simulation settings. Dynamics and hardware-controller equivalence have not been validated. URDF geometry loading does not run ROS control extensions.

Dynamic task execution, policy performance and training behavior have not been validated.
