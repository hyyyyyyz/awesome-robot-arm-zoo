# Kinova Gen3 7-DOF — MuJoCo Menagerie model

These MJCF files are from MuJoCo Menagerie, a collection curated by Google DeepMind. They are a separate source from any manufacturer URDF offered for this hardware.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model — Upstream robot assembly | MJCF | [`models/kinova/gen3_7dof/mjcf/menagerie/gen3.xml`](menagerie/gen3.xml) | MuJoCo 2.3.3 or later; assets resolve relative to the entry. |
| Demonstration scene — Robot with floor, skybox and lighting | MJCF | [`models/kinova/gen3_7dof/mjcf/menagerie/scene.xml`](menagerie/scene.xml) | MuJoCo 2.3.3 or later; assets resolve relative to the entry. |

## Mechanical information

### `gen3.xml`

| Item | Definition |
|---|---|
| Hardware and assembly | Kinova Gen3 7-DOF; upstream robot assembly. |
| Units | Metres, kilograms, radians; the compiler and mesh scale attributes retain upstream values. |
| Base | `base_link`; fixed to the MuJoCo world unless the entry declares a free joint. |
| Movable joint order | `joint_1`, `joint_2`, `joint_3`, `joint_4`, `joint_5`, `joint_6`, `joint_7` (body traversal order). |
| Gripper / coupling | No joint equality coupling is declared. |
| Actuators | `joint_1` controls joint `joint_1`; `joint_2` controls joint `joint_2`; `joint_3` controls joint `joint_3`; `joint_4` controls joint `joint_4`; `joint_5` controls joint `joint_5`; `joint_6` controls joint `joint_6`; `joint_7` controls joint `joint_7` |
| End effector / TCP sites | `pinch_site` |
| Included poses | `home`, `retract` |

| Joint | Type | Range | Units |
|---|---|---|---|
| `joint_1` | hinge | Unbounded in model | radians |
| `joint_2` | hinge | -2.24 2.24 | radians |
| `joint_3` | hinge | Unbounded in model | radians |
| `joint_4` | hinge | -2.57 2.57 | radians |
| `joint_5` | hinge | Unbounded in model | radians |
| `joint_6` | hinge | -2.09 2.09 | radians |
| `joint_7` | hinge | Unbounded in model | radians |

## Loading example

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/kinova/gen3_7dof/mjcf/menagerie/gen3.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| File scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Listed MJCF entries and referenced assets | [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) — Google DeepMind curated | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `kinova_gen3/` | [BSD-3-Clause](menagerie/LICENSE), [NOTICES](menagerie/NOTICES) |

[Upstream model notes](https://github.com/google-deepmind/mujoco_menagerie/blob/6da8b971844845de6ab27315aacc3a3fea4ddb8e/kinova_gen3/README.md) describe the source conversion and model-specific changes. The model-specific license is retained verbatim.

## Model preparation

The selected MJCF entries, their includes, and referenced assets retain upstream contents and relative paths. Mechanical definitions, actuators, equality constraints, collision geometry and keyframes are unchanged. Each demonstration scene retains its upstream ground, light and camera definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/kinova/gen3_7dof/mjcf/menagerie/gen3.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/kinova/gen3_7dof/mjcf/menagerie/scene.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- The MJCF is the curated Menagerie simulation model; its conversion choices and physical approximations are documented in the upstream model notes.
