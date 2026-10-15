# AgileX PiPER arm

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="AgileX PiPER arm model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Official manufacturer model files for the assembly identified below.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model — arm | URDF | [`models/agilex/piper/urdf/arm/piper.urdf`](urdf/arm/piper.urdf) | Local file loader; use a fixed base for mounted arms. |
| Robot model — with_gripper | URDF | [`models/agilex/piper/urdf/with_gripper/piper.urdf`](urdf/with_gripper/piper.urdf) | Local file loader; use a fixed base for mounted arms. |
| Robot model — v100 | URDF | [`models/agilex/piper/urdf/v100/piper.urdf`](urdf/v100/piper.urdf) | Local file loader; use a fixed base for mounted arms. |
| Robot model — with_gripper | MJCF | [`models/agilex/piper/mjcf/with_gripper/piper.xml`](mjcf/with_gripper/piper.xml) | Local file loader; use a fixed base for mounted arms. |
| Robot model — arm | MJCF | [`models/agilex/piper/mjcf/arm/piper.xml`](mjcf/arm/piper.xml) | Local file loader; use a fixed base for mounted arms. |
| Robot model — Upstream robot assembly | MJCF | [`models/agilex/piper/mjcf/menagerie/piper.xml`](mjcf/menagerie/piper.xml) | MuJoCo; complete relative resources are included. |
| Demonstration scene — Robot with floor, skybox and lighting | MJCF | [`models/agilex/piper/mjcf/menagerie/scene.xml`](mjcf/menagerie/scene.xml) | MuJoCo; complete relative resources are included. |

## Mechanical information

The URDF information below describes its manufacturer or maintainer assembly. For the separate curated MJCF assembly, joint names and actuators, see [MJCF model notes](mjcf/README.md).

### arm

| Item | Definition |
|---|---|
| Hardware revision and gripper | AgileX PiPER arm; configuration represented by the entry. |
| Units | URDF SI conventions: metres, kilograms, radians. Mesh scaling is retained from upstream. |
| Base | `dummy_link`; attach this root frame to the consuming scene. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6` (upstream declaration order; fixed joints omitted). |
| Gripper | No mimic coupling is declared. Any gripper joint limits remain in the entry. |
| End effector / TCP | Leaf frames: `link6`. Their upstream transforms are retained. |
| Included poses | No separate pose configuration is included. |
### with_gripper

| Item | Definition |
|---|---|
| Hardware revision and gripper | AgileX PiPER with gripper; configuration represented by the entry. |
| Units | URDF SI conventions: metres, kilograms, radians. Mesh scaling is retained from upstream. |
| Base | `dummy_link`; attach this root frame to the consuming scene. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`, `joint7`, `joint8` (upstream declaration order; fixed joints omitted). |
| Gripper | No mimic coupling is declared. Any gripper joint limits remain in the entry. |
| End effector / TCP | Leaf frames: `link7`, `link8`. Their upstream transforms are retained. |
| Included poses | No separate pose configuration is included. |
### v100

| Item | Definition |
|---|---|
| Hardware revision and gripper | AgileX PiPER v100; configuration represented by the entry. |
| Units | URDF SI conventions: metres, kilograms, radians. Mesh scaling is retained from upstream. |
| Base | `arm_base`; attach this root frame to the consuming scene. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`, `joint7`, `joint8` (upstream declaration order; fixed joints omitted). |
| Gripper | No mimic coupling is declared. Any gripper joint limits remain in the entry. |
| End effector / TCP | Leaf frames: `link7`, `link8`. Their upstream transforms are retained. |
| Included poses | No separate pose configuration is included. |

### URDF / arm joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `joint1` | revolute | -2.618 | 2.168 | radians |
| `joint2` | revolute | 0 | 3.14 | radians |
| `joint3` | revolute | -2.967 | 0 | radians |
| `joint4` | revolute | -1.745 | 1.745 | radians |
| `joint5` | revolute | -1.22 | 1.22 | radians |
| `joint6` | revolute | -2.0944 | 2.0944 | radians |

### URDF / with_gripper joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `joint1` | revolute | -2.618 | 2.618 | radians |
| `joint2` | revolute | 0 | 3.14 | radians |
| `joint3` | revolute | -2.967 | 0 | radians |
| `joint4` | revolute | -1.745 | 1.745 | radians |
| `joint5` | revolute | -1.22 | 1.22 | radians |
| `joint6` | revolute | -2.0944 | 2.0944 | radians |
| `joint7` | prismatic | 0 | 0.035 | metres |
| `joint8` | prismatic | -0.035 | 0 | metres |

### URDF / v100 joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `joint1` | revolute | -2.618 | 2.618 | radians |
| `joint2` | revolute | 0 | 3.14 | radians |
| `joint3` | revolute | -2.697 | 0 | radians |
| `joint4` | revolute | -1.832 | 1.832 | radians |
| `joint5` | revolute | -1.22 | 1.22 | radians |
| `joint6` | revolute | -3.14 | 3.14 | radians |
| `joint7` | prismatic | 0 | 0.05 | metres |
| `joint8` | prismatic | -0.05 | 0 | metres |

### MJCF / with_gripper joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `joint1` | hinge | -2.618 | 2.168 | radians |
| `joint2` | hinge | 0 | 3.14 | radians |
| `joint3` | hinge | -2.967 | 0 | radians |
| `joint4` | hinge | -1.745 | 1.745 | radians |
| `joint5` | hinge | -1.22 | 1.22 | radians |
| `joint6` | hinge | -2.0944 | 2.0944 | radians |
| `joint7` | slide | 0 | 0.035 | metres |
| `joint8` | slide | -0.035 | 0 | metres |

### MJCF / arm joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `joint1` | hinge | -2.618 | 2.168 | radians |
| `joint2` | hinge | 0 | 3.14 | radians |
| `joint3` | hinge | -2.967 | 0 | radians |
| `joint4` | hinge | -1.745 | 1.745 | radians |
| `joint5` | hinge | -1.22 | 1.22 | radians |
| `joint6` | hinge | -2.0944 | 2.0944 | radians |

The MJCF gripper variant has independent `joint7` and `joint8` slide joints with ranges 0–0.035 m and −0.035–0 m; no equality coupling is declared. Its joint control ranges differ from several joint limits, and both definitions are retained. The arm-only MJCF entry has six hinge joints and no gripper. No keyframe poses are declared.

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/agilex/piper/urdf/arm/piper.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/agilex/piper/mjcf/with_gripper/piper.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF / arm entry and referenced resources | [piper_ros](https://github.com/agilexrobotics/piper_ros) | `ac41fcbcdda598f01b51cf6175ed9a24d0dacadc` | `src/piper_description/urdf/piper_no_gripper_description.urdf` | [LICENSE](urdf/arm/LICENSE), [NOTICES](urdf/arm/NOTICES) |
| URDF / with_gripper entry and referenced resources | [piper_ros](https://github.com/agilexrobotics/piper_ros) | `ac41fcbcdda598f01b51cf6175ed9a24d0dacadc` | `src/piper_description/urdf/piper_description.urdf` | [LICENSE](urdf/with_gripper/LICENSE), [NOTICES](urdf/with_gripper/NOTICES) |
| URDF / v100 entry and referenced resources | [piper_ros](https://github.com/agilexrobotics/piper_ros) | `ac41fcbcdda598f01b51cf6175ed9a24d0dacadc` | `src/piper_description/urdf/piper_description_v100.urdf` | [LICENSE](urdf/v100/LICENSE), [NOTICES](urdf/v100/NOTICES) |
| MJCF / with_gripper entry and referenced resources | [piper_ros](https://github.com/agilexrobotics/piper_ros) | `ac41fcbcdda598f01b51cf6175ed9a24d0dacadc` | `src/piper_description/mujoco_model/piper_description.xml` | [LICENSE](mjcf/with_gripper/LICENSE), [NOTICES](mjcf/with_gripper/NOTICES) |
| MJCF / arm entry and referenced resources | [piper_ros](https://github.com/agilexrobotics/piper_ros) | `ac41fcbcdda598f01b51cf6175ed9a24d0dacadc` | `src/piper_description/mujoco_model/piper_no_gripper_description.xml` | [LICENSE](mjcf/arm/LICENSE), [NOTICES](mjcf/arm/NOTICES) |
| Curated MJCF and referenced assets | [Google DeepMind MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `agilex_piper/` | [Model license](mjcf/menagerie/LICENSE), [notices](mjcf/menagerie/NOTICES) |

License: MIT. The license and attribution notices apply to the model entry and copied dependencies from the stated project.

## Model preparation

The MJCF entries and dependencies retain the curator’s model definitions and relative paths. [MJCF model notes](mjcf/README.md) describe that format separately.

 Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

 Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

 Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

 Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

 Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/agilex/piper/urdf/arm/piper.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |
| `models/agilex/piper/urdf/with_gripper/piper.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |
| `models/agilex/piper/urdf/v100/piper.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |
| `models/agilex/piper/mjcf/with_gripper/piper.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/agilex/piper/mjcf/arm/piper.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/agilex/piper/mjcf/menagerie/piper.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/agilex/piper/mjcf/menagerie/scene.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- ROS and Gazebo control extensions, when present, retain their upstream metadata; their external runtime plugins are not included.
- Upstream hardware or revision distinctions beyond the source filename are not independently established.
- The URDF has no inertial element for `dummy_link`.
