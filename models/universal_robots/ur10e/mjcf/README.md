# Universal Robots UR10e — MuJoCo Menagerie model

These MJCF files are from MuJoCo Menagerie, a collection curated by Google DeepMind. They are a separate source from any manufacturer URDF offered for this hardware.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model — Upstream robot assembly | MJCF | [`models/universal_robots/ur10e/mjcf/menagerie/ur10e.xml`](menagerie/ur10e.xml) | MuJoCo 2.3.3 or later; assets resolve relative to the entry. |
| Demonstration scene — Robot with floor, skybox and lighting | MJCF | [`models/universal_robots/ur10e/mjcf/menagerie/scene.xml`](menagerie/scene.xml) | MuJoCo 2.3.3 or later; assets resolve relative to the entry. |

## Mechanical information

### `ur10e.xml`

| Item | Definition |
|---|---|
| Hardware and assembly | Universal Robots UR10e; upstream robot assembly. |
| Units | Metres, kilograms, radians; the compiler and mesh scale attributes retain upstream values. |
| Base | `base`; fixed to the MuJoCo world unless the entry declares a free joint. |
| Movable joint order | `shoulder_pan_joint`, `shoulder_lift_joint`, `elbow_joint`, `wrist_1_joint`, `wrist_2_joint`, `wrist_3_joint` (body traversal order). |
| Gripper / coupling | No joint equality coupling is declared. |
| Actuators | `shoulder_pan` controls joint `shoulder_pan_joint`; `shoulder_lift` controls joint `shoulder_lift_joint`; `elbow` controls joint `elbow_joint`; `wrist_1` controls joint `wrist_1_joint`; `wrist_2` controls joint `wrist_2_joint`; `wrist_3` controls joint `wrist_3_joint` |
| End effector / TCP sites | `attachment_site` |
| Included poses | `home` |

| Joint | Type | Range | Units |
|---|---|---|---|
| `shoulder_pan_joint` | hinge | -6.28319 6.28319 | radians |
| `shoulder_lift_joint` | hinge | -6.28319 6.28319 | radians |
| `elbow_joint` | hinge | -3.1415 3.1415 | radians |
| `wrist_1_joint` | hinge | -6.28319 6.28319 | radians |
| `wrist_2_joint` | hinge | -6.28319 6.28319 | radians |
| `wrist_3_joint` | hinge | -6.28319 6.28319 | radians |

## Loading example

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/universal_robots/ur10e/mjcf/menagerie/ur10e.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| File scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Listed MJCF entries and referenced assets | [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) — Google DeepMind curated | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `universal_robots_ur10e/` | [BSD-3-Clause](menagerie/LICENSE), [NOTICES](menagerie/NOTICES) |

[Upstream model notes](https://github.com/google-deepmind/mujoco_menagerie/blob/6da8b971844845de6ab27315aacc3a3fea4ddb8e/universal_robots_ur10e/README.md) describe the source conversion and model-specific changes. The model-specific license is retained verbatim.

## Model preparation

The selected MJCF entries, their includes, and referenced assets retain upstream contents and relative paths. Mechanical definitions, actuators, equality constraints, collision geometry and keyframes are unchanged. Each demonstration scene retains its upstream ground, light and camera definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/universal_robots/ur10e/mjcf/menagerie/ur10e.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/universal_robots/ur10e/mjcf/menagerie/scene.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- The MJCF is the curated Menagerie simulation model; its conversion choices and physical approximations are documented in the upstream model notes.
