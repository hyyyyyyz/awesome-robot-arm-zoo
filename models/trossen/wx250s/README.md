# Trossen Interbotix WX250S

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Trossen Interbotix WX250S model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Single arm with gripper. Native X-Series parallel gripper.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Single arm with gripper | URDF | [`models/trossen/wx250s/urdf/wx250s.urdf`](urdf/wx250s.urdf) | Native URDF loaders; select a fixed base in the consuming simulator when required. |
| Robot with grippers | MJCF | [`models/trossen/wx250s/mjcf/wx250s.xml`](mjcf/wx250s.xml) | MuJoCo native XML loader; use an absolute entry path. |
| Demonstration scene with ground plane | MJCF | [`models/trossen/wx250s/mjcf/scene.xml`](mjcf/scene.xml) | MuJoCo native XML loader; use an absolute entry path. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | Trossen Interbotix WX250S; Native X-Series parallel gripper |
| Units | Metres, kilograms, radians; native mesh scales are retained. |
| Base | `wx250s/base_link` |
| Movable joint order | `waist`, `shoulder`, `elbow`, `forearm_roll`, `wrist_angle`, `wrist_rotate`, `gripper`, `left_finger`, `right_finger` |
| Gripper relationships | right_finger follows left_finger |
| End effector / TCP | `wx250s/gripper_link`, `wx250s/ee_gripper_link` |
| Included poses | No separate pose configuration is included. |

The native Menagerie MJCF is a separate simulation definition: its arm joints are `waist`, `shoulder`, `elbow`, `forearm_roll`, `wrist_angle`, `wrist_rotate`, followed by equality-coupled `left_finger` and `right_finger` joints. It retains the upstream position actuators, collision approximations and `home` keyframe. The manufacturer URDF mechanical definition above remains the reference for the URDF entry.

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/trossen/wx250s/urdf/wx250s.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF and its referenced resources | [Official manufacturer repository](https://github.com/Interbotix/interbotix_ros_manipulators) | `0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9` | `interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro` and referenced model resources | [Upstream terms](urdf/LICENSE) |
| MJCF and referenced resources | [Upstream project](https://github.com/google-deepmind/mujoco_menagerie) | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `trossen_wx250s` | [BSD-3-Clause](mjcf/LICENSE) |

Upstream copyright notices and redistribution terms are retained. Any independently licensed resource notices used by this assembly are preserved under `urdf/licenses/`.

## Model preparation

The static URDF retains the upstream links, joints, inertia, limits, collision shapes and mesh scales. Resource references resolve within the format directory. Xacro sources are expanded with xacro 2.1.1 where applicable. Source argument values: `{}`. The MuJoCo-specific mesh-directory override, when present in the source, is omitted so that the prepared mesh paths are used.

The MJCF robot and ground-plane scene retain native Menagerie XML, meshes and textures. They are independent of the manufacturer URDF definitions and include Menagerie’s actuator tuning and collision modeling.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/trossen/wx250s/urdf/wx250s.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |
| `models/trossen/wx250s/mjcf/wx250s.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Copy the complete format directory, change caller directory, compile XML and call `mj_forward`. | Passed, including resource relocation. |
| `models/trossen/wx250s/mjcf/scene.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Copy the complete format directory, change caller directory, compile XML and call `mj_forward`. | Passed, including resource relocation. |

The MJCF relocation and forward-kinematics checks were performed on 2026-10-16.

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

ROS/Gazebo extensions in the source model require the corresponding runtime if used; direct URDF geometry loading does not execute those plugins. The consuming project supplies its controller and task configuration.
