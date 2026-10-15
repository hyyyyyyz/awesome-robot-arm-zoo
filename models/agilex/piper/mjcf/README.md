# AgileX PiPER — MuJoCo Menagerie model

These MJCF files are from MuJoCo Menagerie, a collection curated by Google DeepMind. They are a separate source from any manufacturer URDF offered for this hardware.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model — Upstream robot assembly | MJCF | [`models/agilex/piper/mjcf/menagerie/piper.xml`](menagerie/piper.xml) | MuJoCo 2.3.4 or later; assets resolve relative to the entry. |
| Demonstration scene — Robot with floor, skybox and lighting | MJCF | [`models/agilex/piper/mjcf/menagerie/scene.xml`](menagerie/scene.xml) | MuJoCo 2.3.4 or later; assets resolve relative to the entry. |

## Mechanical information

### `piper.xml`

| Item | Definition |
|---|---|
| Hardware and assembly | AgileX PiPER; upstream robot assembly. |
| Units | Metres, kilograms, radians; the compiler and mesh scale attributes retain upstream values. |
| Base | `base_link`; fixed to the MuJoCo world unless the entry declares a free joint. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`, `joint7`, `joint8` (body traversal order). |
| Gripper / coupling | `joint8` equals the polynomial 0 -1 0 0 0 of `joint7` |
| Actuators | `joint1` controls joint `joint1`; `joint2` controls joint `joint2`; `joint3` controls joint `joint3`; `joint4` controls joint `joint4`; `joint5` controls joint `joint5`; `joint6` controls joint `joint6`; `gripper` controls joint `joint7` |
| End effector / TCP sites | No named TCP site is declared; use the terminal body frame defined in the entry. |
| Included poses | `home` |

| Joint | Type | Range | Units |
|---|---|---|---|
| `joint1` | hinge | -2.618 2.618 | radians |
| `joint2` | hinge | 0 3.14 | radians |
| `joint3` | hinge | -2.697 0 | radians |
| `joint4` | hinge | -1.832 1.832 | radians |
| `joint5` | hinge | -1.22 1.22 | radians |
| `joint6` | hinge | -3.14 3.14 | radians |
| `joint7` | slide | 0 0.035 | metres |
| `joint8` | slide | -0.035 0 | metres |

## Loading example

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/agilex/piper/mjcf/with_gripper/piper.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| File scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Listed MJCF entries and referenced assets | [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) — Google DeepMind curated | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `agilex_piper/` | [MIT](menagerie/LICENSE), [NOTICES](menagerie/NOTICES) |

[Upstream model notes](https://github.com/google-deepmind/mujoco_menagerie/blob/6da8b971844845de6ab27315aacc3a3fea4ddb8e/agilex_piper/README.md) describe the source conversion and model-specific changes. The model-specific license is retained verbatim.

## Model preparation

The selected MJCF entries, their includes, and referenced assets retain upstream contents and relative paths. Mechanical definitions, actuators, equality constraints, collision geometry and keyframes are unchanged. Each demonstration scene retains its upstream ground, light and camera definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/agilex/piper/mjcf/with_gripper/piper.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/agilex/piper/mjcf/arm/piper.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/agilex/piper/mjcf/menagerie/piper.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/agilex/piper/mjcf/menagerie/scene.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- The MJCF is the curated Menagerie simulation model; its conversion choices and physical approximations are documented in the upstream model notes.
