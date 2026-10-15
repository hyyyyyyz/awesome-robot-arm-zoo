# Universal Robots UR5E

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Universal Robots UR5E model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

UR5E 6-joint arm without an end effector. The entry preserves the upstream kinematic, visual, collision, inertial and joint-limit definitions.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model: UR5E 6-joint arm without an end effector | URDF | [`models/universal_robots/ur5e/urdf/ur5e.urdf`](urdf/ur5e.urdf) | A native URDF loader with relative mesh resolution; attach the base to the consuming scene. |
| Robot model — Upstream robot assembly | MJCF | [`models/universal_robots/ur5e/mjcf/menagerie/ur5e.xml`](mjcf/menagerie/ur5e.xml) | MuJoCo; complete relative resources are included. |
| Demonstration scene — Robot with floor, skybox and lighting | MJCF | [`models/universal_robots/ur5e/mjcf/menagerie/scene.xml`](mjcf/menagerie/scene.xml) | MuJoCo; complete relative resources are included. |

## Mechanical information

The URDF information below describes its manufacturer or maintainer assembly. For the separate curated MJCF assembly, joint names and actuators, see [MJCF model notes](mjcf/README.md).

| Item | Definition |
|---|---|
| Hardware revision and gripper | UR5E 6-joint arm without an end effector |
| Units | Metres, kilograms, radians; revolute joint effort in N·m and prismatic effort in N. Mesh scale attributes remain as supplied upstream. |
| Base | `world`; root of the URDF tree. Any supplied fixed base transform is retained. |
| Arm joint order | `shoulder_pan_joint` → `shoulder_lift_joint` → `elbow_joint` → `wrist_1_joint` → `wrist_2_joint` → `wrist_3_joint` |
| Gripper | No gripper is included. |
| End effector / TCP | `flange`, `tool0`; fixed transforms remain in the entry. |
| Included poses | No named poses are defined by this URDF entry. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/universal_robots/ur5e/urdf/ur5e.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/universal_robots/ur5e/mjcf/menagerie/ur5e.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Static URDF and its bundled resources (ur_description) | [https://github.com/UniversalRobots/Universal_Robots_ROS2_Description](https://github.com/UniversalRobots/Universal_Robots_ROS2_Description) | `d4042c1f5123c86645cc5dbd650b4f461f697ee9` | `urdf/ur.urdf.xacro`; model mesh paths under the named packages | [LICENSE](urdf/LICENSE) |
| Curated MJCF and referenced assets | [Google DeepMind MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `universal_robots_ur5e/` | [Model license](mjcf/menagerie/LICENSE), [notices](mjcf/menagerie/NOTICES) |

Bundled upstream resource directories: `meshes/ur5e/collision`, `meshes/ur5e/visual`.

License scope: BSD-3-Clause for the URDF and ordinary mesh families. The complete upstream license texts and notices accompany this format directory.

## Model preparation

The MJCF entries and dependencies retain the curator’s model definitions and relative paths. [MJCF model notes](mjcf/README.md) describe that format separately.

The static entry was expanded with xacro 2.1.1 using ur_type:=ur5e, name:=ur5e. Resources were copied only when referenced by the entry or by one of its mesh/material files. Resource references are local relative paths. Mesh contents and physical parameters retain the upstream definitions. The manufacturer default per-model joint-limit, kinematic, physical and visual YAML files select the mechanical definitions. The upstream world-to-base fixed attachment is retained.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/universal_robots/ur5e/urdf/ur5e.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |
| `models/universal_robots/ur5e/mjcf/menagerie/ur5e.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/universal_robots/ur5e/mjcf/menagerie/scene.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

ROS, Gazebo and physics simulators have not been verified for this entry. The default nominal kinematic parameters are supplied, rather than serial-number-specific robot calibration.
