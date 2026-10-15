# Stäubli TX2 60L

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Stäubli TX2 60L model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

6-joint arm without a gripper. The entry preserves the upstream kinematic, visual, collision, inertial and joint-limit definitions.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model: 6-joint arm without a gripper | URDF | [`models/staubli/tx2_60l/urdf/tx2_60l.urdf`](urdf/tx2_60l.urdf) | A native URDF loader with relative mesh resolution; attach the base to the consuming scene. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | 6-joint arm without a gripper |
| Units | Metres, kilograms, radians; revolute joint effort in N·m and prismatic effort in N. Mesh scale attributes remain as supplied upstream. |
| Base | `base_link`; root of the URDF tree. Any supplied fixed base transform is retained. |
| Arm joint order | `joint_1` → `joint_2` → `joint_3` → `joint_4` → `joint_5` → `joint_6` |
| Gripper | No gripper is included. |
| End effector / TCP | `flange`, `tool0`; fixed transforms remain in the entry. |
| Included poses | No named poses are defined by this URDF entry. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/staubli/tx2_60l/urdf/tx2_60l.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Static URDF and its bundled resources (staubli_tx2_60_support, staubli_tx60_support) | [https://github.com/ros-industrial/staubli_experimental](https://github.com/ros-industrial/staubli_experimental) | `256a71acea2161b64e12af1a6b925a7f26695007` | `staubli_tx2_60_support/urdf/tx2_60l.xacro`; model mesh paths under the named packages | [LICENSE](urdf/LICENSE), [LICENSE.staubli](urdf/LICENSE.staubli) |
| Common material definitions | [ros-industrial/staubli](https://github.com/ros-industrial/staubli) | `367d92ec7432867d9ba87c3399d49a940c4afc67` | `staubli_resources/urdf/common_materials.xacro` and `common_colours.xacro` | [LICENSE.staubli](urdf/LICENSE.staubli) |

Bundled upstream resource directories: `staubli_tx2_60_support/meshes/tx2_60/collision`, `staubli_tx2_60_support/meshes/tx2_60/visual`, `staubli_tx2_60_support/meshes/tx2_60l/collision`, `staubli_tx2_60_support/meshes/tx2_60l/visual`, `staubli_tx60_support/meshes/tx60/collision`, `staubli_tx60_support/meshes/tx60/visual`.

License scope: Apache-2.0 for the experimental model and common materials from ros-industrial/staubli. The complete upstream license texts and notices accompany this format directory.

## Model preparation

The static entry was expanded with xacro 2.1.1 using upstream defaults. Resources were copied only when referenced by the entry or by one of its mesh/material files. Resource references are local relative paths. Mesh contents and physical parameters retain the upstream definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/staubli/tx2_60l/urdf/tx2_60l.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

ROS, Gazebo and physics simulators have not been verified for this entry. These are ROS-Industrial experimental nominal-speed model definitions. Upstream supplies no masses, centres of mass or inertias; axis 5 effort is 8 N·m to permit maximum axis 6 effort.

The source omits inertial definitions on these moving links with geometry: `link_1`, `link_2`, `link_3`, `link_4`, `link_5`, `link_6`. It does not supply a complete dynamics model.
