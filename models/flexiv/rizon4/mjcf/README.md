# Flexiv Rizon 4 — MuJoCo Menagerie model

These MJCF files are from MuJoCo Menagerie, a collection curated by Google DeepMind. They are a separate source from any manufacturer URDF offered for this hardware.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model — Upstream robot assembly | MJCF | [`models/flexiv/rizon4/mjcf/menagerie/flexiv_rizon4.xml`](menagerie/flexiv_rizon4.xml) | MuJoCo 3.1.3 or later; assets resolve relative to the entry. |
| Demonstration scene — Robot with floor, skybox and lighting | MJCF | [`models/flexiv/rizon4/mjcf/menagerie/scene.xml`](menagerie/scene.xml) | MuJoCo 3.1.3 or later; assets resolve relative to the entry. |

## Mechanical information

### `flexiv_rizon4.xml`

| Item | Definition |
|---|---|
| Hardware and assembly | Flexiv Rizon 4; upstream robot assembly. |
| Units | Metres, kilograms, radians; the compiler and mesh scale attributes retain upstream values. |
| Base | `base`; fixed to the MuJoCo world unless the entry declares a free joint. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`, `joint7` (body traversal order). |
| Gripper / coupling | No joint equality coupling is declared. |
| Actuators | `joint1` controls joint `joint1`; `joint2` controls joint `joint2`; `joint3` controls joint `joint3`; `joint4` controls joint `joint4`; `joint5` controls joint `joint5`; `joint6` controls joint `joint6`; `joint7` controls joint `joint7` |
| End effector / TCP sites | No named TCP site is declared; use the terminal body frame defined in the entry. |
| Included poses | `home` |

| Joint | Type | Range | Units |
|---|---|---|---|
| `joint1` | hinge | -2.8798 2.8798 | radians |
| `joint2` | hinge | -2.3562 2.3562 | radians |
| `joint3` | hinge | -3.0543 3.0543 | radians |
| `joint4` | hinge | -1.9548 2.7751 | radians |
| `joint5` | hinge | -3.0543 3.0543 | radians |
| `joint6` | hinge | -1.4835 4.6251 | radians |
| `joint7` | hinge | -3.0543 3.0543 | radians |

## Loading example

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/flexiv/rizon4/mjcf/menagerie/flexiv_rizon4.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| File scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Listed MJCF entries and referenced assets | [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) — Google DeepMind curated | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `flexiv_rizon4/` | [Apache-2.0](menagerie/LICENSE), [NOTICES](menagerie/NOTICES) |

[Upstream model notes](https://github.com/google-deepmind/mujoco_menagerie/blob/6da8b971844845de6ab27315aacc3a3fea4ddb8e/flexiv_rizon4/README.md) describe the source conversion and model-specific changes. The model-specific license is retained verbatim.

## Model preparation

The selected MJCF entries, their includes, and referenced assets retain upstream contents and relative paths. Mechanical definitions, actuators, equality constraints, collision geometry and keyframes are unchanged. Each demonstration scene retains its upstream ground, light and camera definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/flexiv/rizon4/mjcf/menagerie/flexiv_rizon4.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/flexiv/rizon4/mjcf/menagerie/scene.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- The MJCF is the curated Menagerie simulation model; its conversion choices and physical approximations are documented in the upstream model notes.
