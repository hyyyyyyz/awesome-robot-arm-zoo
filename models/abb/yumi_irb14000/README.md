# ABB YUMI IRB14000

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="ABB YUMI IRB14000 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

YuMi IRB 14000 dual 7-joint arms with two modeled parallel servo grippers. The entry preserves the upstream kinematic, visual, collision, inertial and joint-limit definitions.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model: YuMi IRB 14000 dual 7-joint arms with two modeled parallel servo grippers | URDF | [`models/abb/yumi_irb14000/urdf/yumi_irb14000.urdf`](urdf/yumi_irb14000.urdf) | A native URDF loader with relative mesh resolution; attach the base to the consuming scene. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | YuMi IRB 14000 dual 7-joint arms with two modeled parallel servo grippers |
| Units | Metres, kilograms, radians; revolute joint effort in N·m and prismatic effort in N. Mesh scale attributes remain as supplied upstream. |
| Base | `world`; root of the URDF tree. Any supplied fixed base transform is retained. |
| Arm joint order | Right: `yumi_joint_1_r` → `yumi_joint_2_r` → `yumi_joint_7_r` → `yumi_joint_3_r` → `yumi_joint_4_r` → `yumi_joint_5_r` → `yumi_joint_6_r`; left: `yumi_joint_1_l` → `yumi_joint_2_l` → `yumi_joint_7_l` → `yumi_joint_3_l` → `yumi_joint_4_l` → `yumi_joint_5_l` → `yumi_joint_6_l`. The physical serial order includes joint 7 between joints 2 and 3. |
| Gripper | `gripper_r_joint` and `gripper_l_joint`: 0 to 0.025 m per jaw. `gripper_r_joint_m` and `gripper_l_joint_m` mimic the respective active joint with multiplier 1 and offset 0; modeled full opening is 0.05 m. |
| End effector / TCP | `yumi_link_7_r` / `yumi_link_7_l` are the arm attachment links; fixed gripper mounting transforms are retained. |
| Included poses | No named poses are defined by this URDF entry. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/abb/yumi_irb14000/urdf/yumi_irb14000.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Static URDF and its bundled resources (yumi_description) | [https://github.com/OrebroUniversity/yumi](https://github.com/OrebroUniversity/yumi) | `fb7f57df05444e6a28df6eda26034de730b8f8fe` | `yumi_description/urdf/yumi.urdf`; model mesh paths under the named packages | [LICENSE](urdf/LICENSE) |

Bundled upstream resource directories: `yumi_description/meshes`, `yumi_description/meshes/coarse`, `yumi_description/meshes/gripper`, `yumi_description/meshes/gripper/coarse`.

License scope: BSD-2-Clause for the model and mesh resources; copyright 2016 Robert Krug and Todor Stoyanov, AASS Research Center, Örebro University, Sweden. The complete upstream license texts and notices accompany this format directory.

## Model preparation

The upstream static URDF is retained with local resource references. Resources were copied only when referenced by the entry or by one of its mesh/material files. Resource references are local relative paths. Mesh contents and physical parameters retain the upstream definitions.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/abb/yumi_irb14000/urdf/yumi_irb14000.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

ROS, Gazebo and physics simulators have not been verified for this entry. This academic model is maintained in the archived Örebro University repository, rather than by ABB. Native Gazebo controller and mimic plugins are outside the verified loading scope.
