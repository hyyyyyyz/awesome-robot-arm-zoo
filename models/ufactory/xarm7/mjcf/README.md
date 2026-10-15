# UFACTORY xArm7 — MuJoCo Menagerie model

These MJCF files are from MuJoCo Menagerie, a collection curated by Google DeepMind. They are a separate source from any manufacturer URDF offered for this hardware.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model — Upstream robot assembly | MJCF | [`models/ufactory/xarm7/mjcf/menagerie/xarm7.xml`](menagerie/xarm7.xml) | MuJoCo 2.3.3 or later; assets resolve relative to the entry. |
| Robot model — Arm without hand | MJCF | [`models/ufactory/xarm7/mjcf/menagerie/xarm7_nohand.xml`](menagerie/xarm7_nohand.xml) | MuJoCo 2.3.3 or later; assets resolve relative to the entry. |
| Demonstration scene — Robot with floor, skybox and lighting | MJCF | [`models/ufactory/xarm7/mjcf/menagerie/scene.xml`](menagerie/scene.xml) | MuJoCo 2.3.3 or later; assets resolve relative to the entry. |

## Mechanical information

### `xarm7.xml`

| Item | Definition |
|---|---|
| Hardware and assembly | UFACTORY xArm7; upstream robot assembly. |
| Units | Metres, kilograms, radians; the compiler and mesh scale attributes retain upstream values. |
| Base | `link_base`; fixed to the MuJoCo world unless the entry declares a free joint. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`, `joint7`, `left_driver_joint`, `left_finger_joint`, `left_inner_knuckle_joint`, `right_driver_joint`, `right_finger_joint`, `right_inner_knuckle_joint` (body traversal order). |
| Gripper / coupling | `left_driver_joint` equals the polynomial 0 1 0 0 0 of `right_driver_joint` |
| Actuators | `act1` controls joint `joint1`; `act2` controls joint `joint2`; `act3` controls joint `joint3`; `act4` controls joint `joint4`; `act5` controls joint `joint5`; `act6` controls joint `joint6`; `act7` controls joint `joint7`; `gripper` controls tendon `split` |
| End effector / TCP sites | `link_tcp` |
| Included poses | `home` |

| Joint | Type | Range | Units |
|---|---|---|---|
| `joint1` | hinge | -6.28319 6.28319 | radians |
| `joint2` | hinge | -2.059 2.0944 | radians |
| `joint3` | hinge | -6.28319 6.28319 | radians |
| `joint4` | hinge | -0.19198 3.927 | radians |
| `joint5` | hinge | -6.28319 6.28319 | radians |
| `joint6` | hinge | -1.69297 3.14159 | radians |
| `joint7` | hinge | -6.28319 6.28319 | radians |
| `left_driver_joint` | hinge | 0 0.85 | radians |
| `left_finger_joint` | hinge | 0 0.85 | radians |
| `left_inner_knuckle_joint` | hinge | 0 0.85 | radians |
| `right_driver_joint` | hinge | 0 0.85 | radians |
| `right_finger_joint` | hinge | 0 0.85 | radians |
| `right_inner_knuckle_joint` | hinge | 0 0.85 | radians |
### `xarm7_nohand.xml`

| Item | Definition |
|---|---|
| Hardware and assembly | UFACTORY xArm7; arm without hand. |
| Units | Metres, kilograms, radians; the compiler and mesh scale attributes retain upstream values. |
| Base | `link_base`; fixed to the MuJoCo world unless the entry declares a free joint. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`, `joint7` (body traversal order). |
| Gripper / coupling | No joint equality coupling is declared. |
| Actuators | `act1` controls joint `joint1`; `act2` controls joint `joint2`; `act3` controls joint `joint3`; `act4` controls joint `joint4`; `act5` controls joint `joint5`; `act6` controls joint `joint6`; `act7` controls joint `joint7` |
| End effector / TCP sites | `attachment_site` |
| Included poses | `home` |

| Joint | Type | Range | Units |
|---|---|---|---|
| `joint1` | hinge | -6.28319 6.28319 | radians |
| `joint2` | hinge | -2.059 2.0944 | radians |
| `joint3` | hinge | -6.28319 6.28319 | radians |
| `joint4` | hinge | -0.19198 3.927 | radians |
| `joint5` | hinge | -6.28319 6.28319 | radians |
| `joint6` | hinge | -1.69297 3.14159 | radians |
| `joint7` | hinge | -6.28319 6.28319 | radians |

## Loading example

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/ufactory/xarm7/mjcf/menagerie/xarm7.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| File scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Listed MJCF entries and referenced assets | [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) — Google DeepMind curated | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `ufactory_xarm7/` | [BSD-3-Clause](menagerie/LICENSE), [NOTICES](menagerie/NOTICES) |

[Upstream model notes](https://github.com/google-deepmind/mujoco_menagerie/blob/6da8b971844845de6ab27315aacc3a3fea4ddb8e/ufactory_xarm7/README.md) describe the source conversion and model-specific changes. The model-specific license is retained verbatim.

## Model preparation

The selected MJCF entries, their includes, and referenced assets retain upstream contents and relative paths. Mechanical definitions, actuators, equality constraints, collision geometry and keyframes are unchanged. Each demonstration scene retains its upstream ground, light and camera definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/ufactory/xarm7/mjcf/menagerie/xarm7.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/ufactory/xarm7/mjcf/menagerie/xarm7_nohand.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/ufactory/xarm7/mjcf/menagerie/scene.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- The MJCF is the curated Menagerie simulation model; its conversion choices and physical approximations are documented in the upstream model notes.
