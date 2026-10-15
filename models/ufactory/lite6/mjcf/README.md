# UFACTORY Lite6 — MuJoCo Menagerie model

These MJCF files are from MuJoCo Menagerie, a collection curated by Google DeepMind. They are a separate source from any manufacturer URDF offered for this hardware.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model — Upstream robot assembly | MJCF | [`models/ufactory/lite6/mjcf/menagerie/lite6.xml`](menagerie/lite6.xml) | MuJoCo 3.1.0 or later; assets resolve relative to the entry. |
| Robot model — Narrow gripper assembly | MJCF | [`models/ufactory/lite6/mjcf/menagerie/lite6_gripper_narrow.xml`](menagerie/lite6_gripper_narrow.xml) | MuJoCo 3.1.0 or later; assets resolve relative to the entry. |
| Robot model — Wide gripper assembly | MJCF | [`models/ufactory/lite6/mjcf/menagerie/lite6_gripper_wide.xml`](menagerie/lite6_gripper_wide.xml) | MuJoCo 3.1.0 or later; assets resolve relative to the entry. |
| Demonstration scene — Robot with floor, skybox and lighting | MJCF | [`models/ufactory/lite6/mjcf/menagerie/scene.xml`](menagerie/scene.xml) | MuJoCo 3.1.0 or later; assets resolve relative to the entry. |

## Mechanical information

### `lite6.xml`

| Item | Definition |
|---|---|
| Hardware and assembly | UFACTORY Lite6; upstream robot assembly. |
| Units | Metres, kilograms, radians; the compiler and mesh scale attributes retain upstream values. |
| Base | `link_base`; fixed to the MuJoCo world unless the entry declares a free joint. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6` (body traversal order). |
| Gripper / coupling | No joint equality coupling is declared. |
| Actuators | `unnamed` controls joint `joint1`; `unnamed` controls joint `joint2`; `unnamed` controls joint `joint3`; `unnamed` controls joint `joint4`; `unnamed` controls joint `joint5`; `unnamed` controls joint `joint6` |
| End effector / TCP sites | `attachment_site` |
| Included poses | `home` |

| Joint | Type | Range | Units |
|---|---|---|---|
| `joint1` | hinge | -6.28319 6.28319 | radians |
| `joint2` | hinge | -2.61799 2.61799 | radians |
| `joint3` | hinge | -0.061087 5.23599 | radians |
| `joint4` | hinge | -6.28319 6.28319 | radians |
| `joint5` | hinge | -2.1642 2.1642 | radians |
| `joint6` | hinge | -6.28319 6.28319 | radians |
### `lite6_gripper_narrow.xml`

| Item | Definition |
|---|---|
| Hardware and assembly | UFACTORY Lite6; narrow gripper assembly. |
| Units | Metres, kilograms, radians; the compiler and mesh scale attributes retain upstream values. |
| Base | `link_base`; fixed to the MuJoCo world unless the entry declares a free joint. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`, `gripper_left_finger`, `gripper_right_finger` (body traversal order). |
| Gripper / coupling | `gripper_left_finger` equals the polynomial 0 -1 0 0 0 of `gripper_right_finger` |
| Actuators | `unnamed` controls joint `joint1`; `unnamed` controls joint `joint2`; `unnamed` controls joint `joint3`; `unnamed` controls joint `joint4`; `unnamed` controls joint `joint5`; `unnamed` controls joint `joint6`; `gripper` controls joint `gripper_left_finger` |
| End effector / TCP sites | `attachment_site`, `end_effector` |
| Included poses | `home` |

| Joint | Type | Range | Units |
|---|---|---|---|
| `joint1` | hinge | -6.28319 6.28319 | radians |
| `joint2` | hinge | -2.61799 2.61799 | radians |
| `joint3` | hinge | -0.061087 5.23599 | radians |
| `joint4` | hinge | -6.28319 6.28319 | radians |
| `joint5` | hinge | -2.1642 2.1642 | radians |
| `joint6` | hinge | -6.28319 6.28319 | radians |
| `gripper_left_finger` | slide | -0.0081 -1e-5 | metres |
| `gripper_right_finger` | slide | 1e-5 0.0081 | metres |
### `lite6_gripper_wide.xml`

| Item | Definition |
|---|---|
| Hardware and assembly | UFACTORY Lite6; wide gripper assembly. |
| Units | Metres, kilograms, radians; the compiler and mesh scale attributes retain upstream values. |
| Base | `link_base`; fixed to the MuJoCo world unless the entry declares a free joint. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`, `gripper_left_finger`, `gripper_right_finger` (body traversal order). |
| Gripper / coupling | `gripper_left_finger` equals the polynomial 0 -1 0 0 0 of `gripper_right_finger` |
| Actuators | `unnamed` controls joint `joint1`; `unnamed` controls joint `joint2`; `unnamed` controls joint `joint3`; `unnamed` controls joint `joint4`; `unnamed` controls joint `joint5`; `unnamed` controls joint `joint6`; `gripper` controls joint `gripper_left_finger` |
| End effector / TCP sites | `attachment_site`, `end_effector` |
| Included poses | `home` |

| Joint | Type | Range | Units |
|---|---|---|---|
| `joint1` | hinge | -6.28319 6.28319 | radians |
| `joint2` | hinge | -2.61799 2.61799 | radians |
| `joint3` | hinge | -0.061087 5.23599 | radians |
| `joint4` | hinge | -6.28319 6.28319 | radians |
| `joint5` | hinge | -2.1642 2.1642 | radians |
| `joint6` | hinge | -6.28319 6.28319 | radians |
| `gripper_left_finger` | slide | -0.0081 -1e-5 | metres |
| `gripper_right_finger` | slide | 1e-5 0.0081 | metres |

## Loading example

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/ufactory/lite6/mjcf/menagerie/lite6.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| File scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Listed MJCF entries and referenced assets | [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) — Google DeepMind curated | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `ufactory_lite6/` | [BSD-3-Clause](menagerie/LICENSE), [NOTICES](menagerie/NOTICES) |

[Upstream model notes](https://github.com/google-deepmind/mujoco_menagerie/blob/6da8b971844845de6ab27315aacc3a3fea4ddb8e/ufactory_lite6/README.md) describe the source conversion and model-specific changes. The model-specific license is retained verbatim.

## Model preparation

The selected MJCF entries, their includes, and referenced assets retain upstream contents and relative paths. Mechanical definitions, actuators, equality constraints, collision geometry and keyframes are unchanged. Each demonstration scene retains its upstream ground, light and camera definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/ufactory/lite6/mjcf/menagerie/lite6.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/ufactory/lite6/mjcf/menagerie/lite6_gripper_narrow.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/ufactory/lite6/mjcf/menagerie/lite6_gripper_wide.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/ufactory/lite6/mjcf/menagerie/scene.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- The MJCF is the curated Menagerie simulation model; its conversion choices and physical approximations are documented in the upstream model notes.
