# Franka Robotics Panda / FER

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Franka Robotics Panda / FER model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Franka Emika Robot (Panda / FER), 7-joint arm with Franka Hand parallel gripper. The entry preserves the upstream kinematic, visual, collision, inertial and joint-limit definitions.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model: Franka Emika Robot (Panda / FER), 7-joint arm with Franka Hand parallel gripper | URDF | [`models/franka/panda/urdf/panda.urdf`](urdf/panda.urdf) | A native URDF loader with relative mesh resolution; attach the base to the consuming scene. |
| Robot model — Upstream robot assembly | MJCF | [`models/franka/panda/mjcf/menagerie/panda.xml`](mjcf/menagerie/panda.xml) | MuJoCo; complete relative resources are included. |
| Demonstration scene — Robot with floor, skybox and lighting | MJCF | [`models/franka/panda/mjcf/menagerie/scene.xml`](mjcf/menagerie/scene.xml) | MuJoCo; complete relative resources are included. |

## Mechanical information

The URDF information below describes its manufacturer or maintainer assembly. For the separate curated MJCF assembly, joint names and actuators, see [MJCF model notes](mjcf/README.md).

| Item | Definition |
|---|---|
| Hardware revision and gripper | Franka Emika Robot (Panda / FER), 7-joint arm with Franka Hand parallel gripper |
| Units | Metres, kilograms, radians; revolute joint effort in N·m and prismatic effort in N. Mesh scale attributes remain as supplied upstream. |
| Base | `base`; root of the URDF tree. Any supplied fixed base transform is retained. |
| Arm joint order | `fer_joint1` → `fer_joint2` → `fer_joint3` → `fer_joint4` → `fer_joint5` → `fer_joint6` → `fer_joint7` |
| Gripper | `fer_finger_joint1`: 0.0 to 0.04 m; `fer_finger_joint2`: 0.0 to 0.04 m; mimics `fer_finger_joint1` (multiplier 1, offset 0) |
| End effector / TCP | `fer_link8`, `fer_hand_tcp`; fixed transforms remain in the entry. |
| Included poses | No named poses are defined by this URDF entry. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/franka/panda/urdf/panda.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/franka/panda/mjcf/menagerie/panda.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Static URDF and its bundled resources (franka_description) | [https://github.com/frankarobotics/franka_description](https://github.com/frankarobotics/franka_description) | `7aeeddc449edf8d62b594f9e36a81da53e7796f9` | `robots/fer/fer.urdf.xacro`; model mesh paths under the named packages | [LICENSE](urdf/LICENSE), [NOTICE](urdf/NOTICE) |
| Curated MJCF and referenced assets | [Google DeepMind MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `franka_emika_panda/` | [Model license](mjcf/menagerie/LICENSE), [notices](mjcf/menagerie/NOTICES) |

Bundled upstream resource directories: `meshes/robot_ee/franka_hand_white/collision`, `meshes/robot_ee/franka_hand_white/visual`, `meshes/robots/fer/collision`, `meshes/robots/fer/visual`.

License scope: Apache-2.0 for robot definitions, meshes and Franka Hand; copyright Franka Robotics GmbH, with the upstream NOTICE retained. The complete upstream license texts and notices accompany this format directory.

## Model preparation

The MJCF entries and dependencies retain the curator’s model definitions and relative paths. [MJCF model notes](mjcf/README.md) describe that format separately.

The static entry was expanded with xacro 2.1.1 using with_sc:=False, ee_id:=franka_hand, hand:=True, no_prefix:=false, robot_type:=fer. Resources were copied only when referenced by the entry or by one of its mesh/material files. Resource references are local relative paths. Mesh contents and physical parameters retain the upstream definitions. Expansion uses the upstream scripts/create_urdf.py convert_xacro_to_urdf function. The standard fine collision meshes are retained; with_sc is false, matching the official generator default.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/franka/panda/urdf/panda.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |
| `models/franka/panda/mjcf/menagerie/panda.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/franka/panda/mjcf/menagerie/scene.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

ROS, Gazebo and physics simulators have not been verified for this entry. FER/Panda is retained by upstream but is no longer supported by Franka Robotics.
