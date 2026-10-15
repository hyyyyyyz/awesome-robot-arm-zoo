# Franka Research 3 v2 — MuJoCo Menagerie model

These MJCF files are from MuJoCo Menagerie, a collection curated by Google DeepMind. They are a separate source from any manufacturer URDF offered for this hardware.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model — Upstream robot assembly | MJCF | [`models/franka/fr3v2/mjcf/menagerie/fr3v2.xml`](menagerie/fr3v2.xml) | MuJoCo 3.1.3 or later; assets resolve relative to the entry. |
| Demonstration scene — Robot with floor, skybox and lighting | MJCF | [`models/franka/fr3v2/mjcf/menagerie/scene.xml`](menagerie/scene.xml) | MuJoCo 3.1.3 or later; assets resolve relative to the entry. |

## Mechanical information

### `fr3v2.xml`

| Item | Definition |
|---|---|
| Hardware and assembly | Franka Research 3 v2; upstream robot assembly. |
| Units | Metres, kilograms, radians; the compiler and mesh scale attributes retain upstream values. |
| Base | `base`; fixed to the MuJoCo world unless the entry declares a free joint. |
| Movable joint order | `fr3v2_joint1`, `fr3v2_joint2`, `fr3v2_joint3`, `fr3v2_joint4`, `fr3v2_joint5`, `fr3v2_joint6`, `fr3v2_joint7` (body traversal order). |
| Gripper / coupling | No joint equality coupling is declared. |
| Actuators | `fr3v2_joint1` controls joint `fr3v2_joint1`; `fr3v2_joint2` controls joint `fr3v2_joint2`; `fr3v2_joint3` controls joint `fr3v2_joint3`; `fr3v2_joint4` controls joint `fr3v2_joint4`; `fr3v2_joint5` controls joint `fr3v2_joint5`; `fr3v2_joint6` controls joint `fr3v2_joint6`; `fr3v2_joint7` controls joint `fr3v2_joint7` |
| End effector / TCP sites | No named TCP site is declared; use the terminal body frame defined in the entry. |
| Included poses | `home` |

| Joint | Type | Range | Units |
|---|---|---|---|
| `fr3v2_joint1` | hinge | -2.9007 2.9007 | radians |
| `fr3v2_joint2` | hinge | -1.8361 1.8361 | radians |
| `fr3v2_joint3` | hinge | -2.9007 2.9007 | radians |
| `fr3v2_joint4` | hinge | -3.0770 -0.1169 | radians |
| `fr3v2_joint5` | hinge | -2.8763 2.8763 | radians |
| `fr3v2_joint6` | hinge | 0.4398 4.6216 | radians |
| `fr3v2_joint7` | hinge | -3.0508 3.0508 | radians |

## Loading example

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/franka/fr3v2/mjcf/menagerie/fr3v2.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| File scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Listed MJCF entries and referenced assets | [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) — Google DeepMind curated | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `franka_fr3_v2/` | [Apache-2.0](menagerie/LICENSE), [NOTICES](menagerie/NOTICES) |

[Upstream model notes](https://github.com/google-deepmind/mujoco_menagerie/blob/6da8b971844845de6ab27315aacc3a3fea4ddb8e/franka_fr3_v2/README.md) describe the source conversion and model-specific changes. The model-specific license is retained verbatim.

## Model preparation

The selected MJCF entries, their includes, and referenced assets retain upstream contents and relative paths. Mechanical definitions, actuators, equality constraints, collision geometry and keyframes are unchanged. Each demonstration scene retains its upstream ground, light and camera definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/franka/fr3v2/mjcf/menagerie/fr3v2.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/franka/fr3v2/mjcf/menagerie/scene.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- The MJCF is the curated Menagerie simulation model; its conversion choices and physical approximations are documented in the upstream model notes.
