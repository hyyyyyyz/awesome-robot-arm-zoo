# LeKiwi

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="LeKiwi model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Complete LeKiwi mobile manipulator exported from CAD: three omni wheels, a six-joint SO-100-style follower arm, chassis, battery, electronics mounts and cameras.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Complete mobile manipulator | URDF | [`models/lekiwi/lekiwi/urdf/LeKiwi.urdf`](urdf/LeKiwi.urdf) | Native URDF loader; load visual and collision resources. Root motion as documented below. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | LeKiwi CAD assembly with native rotary jaw gripper |
| Units | Metres, kilograms and radians; native mesh scales are retained. |
| Base | `base_plate_layer1-v5`; URDF has no floating or planar root joint. Choose a floating root in a simulator to move the chassis. |
| Movable joint order | `base_back_wheel`, `base_right_wheel`, `base_left_wheel`, `arm_shoulder_pan`, `arm_shoulder_lift`, `arm_elbow_flex`, `arm_wrist_flex`, `arm_wrist_roll`, `arm_gripper` |
| Gripper | `arm_gripper` is continuous in the source; no numeric travel limit or mimic is declared. |
| End effector / TCP | `Moving_Jaw_08d-v1` is the moving jaw; no separately calibrated TCP is supplied. |
| Included poses | No separate pose configuration is included. |

## Loading example

```python
from yourdfpy import URDF
robot = URDF.load('/absolute/path/to/awesome-robot-arm-zoo/models/lekiwi/lekiwi/urdf/LeKiwi.urdf',
                  load_meshes=True, load_collision_meshes=True,
                  build_collision_scene_graph=True)
robot.update_cfg({})
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF entry and referenced meshes | [LeKiwi](https://github.com/SIGRobotics-UIUC/LeKiwi) | `efa608d7ee5a495a4803b1d28cd0c955b4f1e033` | [`URDF/LeKiwi.urdf`](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/efa608d7ee5a495a4803b1d28cd0c955b4f1e033/URDF/LeKiwi.urdf) and referenced resources | [Apache-2.0](urdf/LICENSE); [upstream license](https://github.com/SIGRobotics-UIUC/LeKiwi/blob/efa608d7ee5a495a4803b1d28cd0c955b4f1e033/LICENSE.txt) |

The upstream project’s Apache-2.0 terms accompany each format directory.

## Model preparation

The upstream URDF and its referenced meshes are packaged for standalone file loading. Relative resource paths are retained; XML formatting is normalized. Source joints, inertia, limits, mesh scales and collision definitions are retained. Only resources needed by the listed entries are included.

## Loading verification

| Entry | Environment and simulator version | Verification steps | Result |
|---|---|---|---|
| [`LeKiwi.urdf`](urdf/LeKiwi.urdf) | macOS; yourdfpy 0.0.60 | Copy the entire format directory, load from an unrelated working directory, configure movable joints, inspect visual and collision bounds. | Passed; 45 links, 9 actuated joints, 45 visual and 45 collision geometries. |

## Known limitations

All nine movable joints are continuous in the CAD export and carry no numeric travel limits. The URDF does not model omni-wheel roller contact or declare a free base. Mobile locomotion and contact dynamics have not been validated. Loading records establish resource completeness and native kinematics; they do not establish task or policy performance.
