# Dobot MG400

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Dobot MG400 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Official manufacturer model files for the assembly identified below.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model | URDF | [`models/dobot/mg400/urdf/mg400.urdf`](urdf/mg400.urdf) | Local file loader; use a fixed base for mounted arms. |

## Mechanical information

### Dobot MG400

| Item | Definition |
|---|---|
| Hardware revision and gripper | Dobot MG400; configuration represented by the entry. |
| Units | URDF SI conventions: metres, kilograms, radians. Mesh scaling is retained from upstream. |
| Base | `base_link`; attach this root frame to the consuming scene. |
| Movable joint order | `j1`, `j2`, `j3_1`, `j3`, `j4_1`, `j4`, `j2_2`, `j3_2`, `j4_2` (upstream declaration order; fixed joints omitted). |
| Gripper | j3_1 mimics j3_2 (multiplier 1, offset 0); j4_1 mimics j4_2 (multiplier -1, offset 0); j2_2 mimics j2 (multiplier 1, offset 0); j3_2 mimics j2_2 (multiplier -1, offset 0); j4_2 mimics j3 (multiplier 1, offset 0) |
| End effector / TCP | Leaf frames: `link5`, `link4_2`. Their upstream transforms are retained. |
| Included poses | No separate pose configuration is included. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/dobot/mg400/urdf/mg400.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF entry and referenced resources | [dobot_mg400_ros](https://github.com/Dobot-Arm/MG400_ROS) | `2bcf6a988311096a6096a2dc4de60dc76f72e80e` | `mg400_description/urdf/mg400_description.urdf` | [LICENSE](urdf/LICENSE), [NOTICES](urdf/NOTICES) |

License: MIT. The license and attribution notices apply to the model entry and copied dependencies from the stated project.

## Model preparation

 Referenced resources are stored inside the format directory and resource URIs are relative to the entry. Joint limits, inertial values, visual and collision geometry retain their upstream definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/dobot/mg400/urdf/mg400.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- ROS and Gazebo control extensions, when present, retain their upstream metadata; their external runtime plugins are not included.
- Upstream hardware or revision distinctions beyond the source filename are not independently established.
- The URDF has no inertial element for `fake_link`.
