# AUBO i10

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="AUBO i10 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Official manufacturer model files for the assembly identified below.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model | URDF | [`models/aubo/i10/urdf/i10.urdf`](urdf/i10.urdf) | Local file loader; use a fixed base for mounted arms. |

## Mechanical information

### AUBO i10

| Item | Definition |
|---|---|
| Hardware revision and gripper | AUBO i10; configuration represented by the entry. |
| Units | URDF SI conventions: metres, kilograms, radians. Mesh scaling is retained from upstream. |
| Base | `base_link`; attach this root frame to the consuming scene. |
| Movable joint order | `shoulder_joint`, `upperArm_joint`, `foreArm_joint`, `wrist1_joint`, `wrist2_joint`, `wrist3_joint` (upstream declaration order; fixed joints omitted). |
| Gripper | No mimic coupling is declared. Any gripper joint limits remain in the entry. |
| End effector / TCP | Leaf frames: `wrist3_Link`. Their upstream transforms are retained. |
| Included poses | No separate pose configuration is included. |

### URDF joint limits

| Joint | Type | Lower | Upper | Units |
|---|---|---|---|---|
| `shoulder_joint` | revolute | -3.04 | 3.04 | radians |
| `upperArm_joint` | revolute | -3.04 | 3.04 | radians |
| `foreArm_joint` | revolute | -3.04 | 3.04 | radians |
| `wrist1_joint` | revolute | -3.04 | 3.04 | radians |
| `wrist2_joint` | revolute | -3.04 | 3.04 | radians |
| `wrist3_joint` | revolute | -3.04 | 3.04 | radians |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/aubo/i10/urdf/i10.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF entry and referenced resources | [aubo_robot](https://github.com/AuboRobot/aubo_robot) | `32210c0b465bc4eef4de01a0917a878c3b24e799` | `aubo_robot/aubo_description/urdf/aubo_i10.urdf` | [LICENSE](urdf/LICENSE), [NOTICES](urdf/NOTICES) |

License: BSD-3-Clause. The license and attribution notices apply to the model entry and copied dependencies from the stated project.

## Model preparation

 Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/aubo/i10/urdf/i10.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Bundled COLLADA meshes declare length units in their asset metadata. The plain yourdfpy 0.0.60 / trimesh 5.1.1 loader does not apply those units; the preview renderer applies them to meshes and file-local transforms. Consuming loaders must honor the declared units. Recorded loading checks cover resource resolution and joint configuration updates, not dimensional accuracy.

Dynamic task execution, controller performance and training behavior have not been validated.

- ROS and Gazebo control extensions, when present, retain their upstream metadata; their external runtime plugins are not included.
- Upstream hardware or revision distinctions beyond the source filename are not independently established.
