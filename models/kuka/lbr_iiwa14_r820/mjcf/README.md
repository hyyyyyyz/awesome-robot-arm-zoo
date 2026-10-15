# KUKA LBR iiwa 14 — MuJoCo Menagerie model

These MJCF files are from MuJoCo Menagerie, a collection curated by Google DeepMind. They are a separate source from any manufacturer URDF offered for this hardware.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model — Upstream robot assembly | MJCF | [`models/kuka/lbr_iiwa14_r820/mjcf/menagerie/iiwa14.xml`](menagerie/iiwa14.xml) | MuJoCo 2.3.3 or later; assets resolve relative to the entry. |
| Demonstration scene — Robot with floor, skybox and lighting | MJCF | [`models/kuka/lbr_iiwa14_r820/mjcf/menagerie/scene.xml`](menagerie/scene.xml) | MuJoCo 2.3.3 or later; assets resolve relative to the entry. |

## Mechanical information

### `iiwa14.xml`

| Item | Definition |
|---|---|
| Hardware and assembly | KUKA LBR iiwa 14; upstream robot assembly. |
| Units | Metres, kilograms, radians; the compiler and mesh scale attributes retain upstream values. |
| Base | `base`; fixed to the MuJoCo world unless the entry declares a free joint. |
| Movable joint order | `joint1`, `joint2`, `joint3`, `joint4`, `joint5`, `joint6`, `joint7` (body traversal order). |
| Gripper / coupling | No joint equality coupling is declared. |
| Actuators | `actuator1` controls joint `joint1`; `actuator2` controls joint `joint2`; `actuator3` controls joint `joint3`; `actuator4` controls joint `joint4`; `actuator5` controls joint `joint5`; `actuator6` controls joint `joint6`; `actuator7` controls joint `joint7` |
| End effector / TCP sites | `attachment_site` |
| Included poses | `home` |

| Joint | Type | Range | Units |
|---|---|---|---|
| `joint1` | hinge | -2.96706 2.96706 | radians |
| `joint2` | hinge | -2.0944 2.0944 | radians |
| `joint3` | hinge | -2.96706 2.96706 | radians |
| `joint4` | hinge | -2.0944 2.0944 | radians |
| `joint5` | hinge | -2.96706 2.96706 | radians |
| `joint6` | hinge | -2.0944 2.0944 | radians |
| `joint7` | hinge | -3.05433 3.05433 | radians |

## Loading example

```python
import mujoco

model = mujoco.MjModel.from_xml_path(
    '/absolute/path/to/awesome-robot-arm-zoo/models/kuka/lbr_iiwa14_r820/mjcf/menagerie/iiwa14.xml'
)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
```

## Sources and licensing

| File scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Listed MJCF entries and referenced assets | [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) — Google DeepMind curated | `6da8b971844845de6ab27315aacc3a3fea4ddb8e` | `kuka_iiwa_14/` | [BSD-3-Clause](menagerie/LICENSE), [NOTICES](menagerie/NOTICES) |

[Upstream model notes](https://github.com/google-deepmind/mujoco_menagerie/blob/6da8b971844845de6ab27315aacc3a3fea4ddb8e/kuka_iiwa_14/README.md) describe the source conversion and model-specific changes. The model-specific license is retained verbatim.

## Model preparation

The selected MJCF entries, their includes, and referenced assets retain upstream contents and relative paths. Mechanical definitions, actuators, equality constraints, collision geometry and keyframes are unchanged. Each demonstration scene retains its upstream ground, light and camera definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/kuka/lbr_iiwa14_r820/mjcf/menagerie/iiwa14.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |
| `models/kuka/lbr_iiwa14_r820/mjcf/menagerie/scene.xml` | macOS 27.2, arm64, Python 3.12.14; MuJoCo 3.16.0 | Compile the model, construct MjData and run mj_forward. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- The MJCF is the curated Menagerie simulation model; its conversion choices and physical approximations are documented in the upstream model notes.
