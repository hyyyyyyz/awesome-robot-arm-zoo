# Rethink Robotics Sawyer — MuJoCo Menagerie model

These MJCF files are from MuJoCo Menagerie, a collection curated by Google DeepMind. They are a separate source from any manufacturer URDF offered for this hardware.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model — Upstream robot assembly | MJCF | [`models/rethink_robotics/sawyer/mjcf/menagerie/sawyer.xml`](menagerie/sawyer.xml) | MuJoCo 2.3.3 or later; assets resolve relative to the entry. |
| Demonstration scene — Robot with floor, skybox and lighting | MJCF | [`models/rethink_robotics/sawyer/mjcf/menagerie/scene.xml`](menagerie/scene.xml) | MuJoCo 2.3.3 or later; assets resolve relative to the entry. |

## Mechanical information

### `sawyer.xml`

| Item | Definition |
|---|---|
| Hardware and assembly | Rethink Robotics Sawyer; upstream robot assembly. |
| Units | Metres, kilograms, radians; the compiler and mesh scale attributes retain upstream values. |
| Base | `base`; fixed to the MuJoCo world unless the entry declares a free joint. |
| Movable joint order | `right_j0`, `right_j1`, `right_j2`, `right_j3`, `right_j4`, `right_j5`, `right_j6` (body traversal order). |
| Gripper / coupling | No joint equality coupling is declared. |
| Actuators | `a0` controls joint `right_j0`; `a1` controls joint `right_j1`; `a2` controls joint `right_j2`; `a3` controls joint `right_j3`; `a4` controls joint `right_j4`; `a5` controls joint `right_j5`; `a6` controls joint `right_j6` |
| End effector / TCP sites | `attachment_site` |
| Included poses | `home` |

| Joint | Type | Range | Units |
|---|---|---|---|
| `right_j0` | hinge | -3.0503 3.0503 | radians |
| `right_j1` | hinge | -3.8095 2.2736 | radians |
| `right_j2` | hinge | -3.0426 3.0426 | radians |
| `right_j3` | hinge | -3.0439 3.0439 | radians |
| `right_j4` | hinge | -2.9761 2.9761 | radians |
| `right_j5` | hinge | -2.9761 2.9761 | radians |
| `right_j6` | hinge | -4.7124 4.7124 | radians |

## Loading example

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/rethink_robotics/sawyer/mjcf/menagerie/sawyer.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| File scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Listed MJCF entries and referenced assets | [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) — Google DeepMind curated | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `rethink_robotics_sawyer/` | [Apache-2.0](menagerie/LICENSE), [NOTICES](menagerie/NOTICES) |

[Upstream model notes](https://github.com/google-deepmind/mujoco_menagerie/blob/6da8b971844845de6ab27315aacc3a3fea4ddb8e/rethink_robotics_sawyer/README.md) describe the source conversion and model-specific changes. The model-specific license is retained verbatim.

## Model preparation

The selected MJCF entries, their includes, and referenced assets retain upstream contents and relative paths. Mechanical definitions, actuators, equality constraints, collision geometry and keyframes are unchanged. Each demonstration scene retains its upstream ground, light and camera definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/rethink_robotics/sawyer/mjcf/menagerie/sawyer.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/rethink_robotics/sawyer/mjcf/menagerie/scene.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- The MJCF is the curated Menagerie simulation model; its conversion choices and physical approximations are documented in the upstream model notes.
