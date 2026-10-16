# Source coverage

This collection contains model files from 23 manufacturers. Manufacturer-maintained descriptions are prioritized; ROS-Industrial, university and Google DeepMind Menagerie sources are identified separately in each model's source table. Sources are pinned to the upstream commits recorded in the model READMEs.

Each model directory lists its actual hardware or assembly, file entries, resource scope and applicable licenses. A manufacturer's presence in the catalog identifies the included models, rather than its entire product range.

## Source families

| Source | Included scope | Source records |
|---|---|---|
| Manufacturer repositories | Prepared static URDFs and their referenced visual/collision resources; existing native files where supplied | Brand and model READMEs |
| Örebro University | ABB YuMi dual-arm description | [YuMi model notes](../models/abb/yumi_irb14000/README.md) |
| Google DeepMind MuJoCo Menagerie | Selected MJCF robot assemblies and separate demonstration scenes | Each included model's `mjcf/README.md` |

The same hardware may have independently sourced URDF and MJCF definitions. Their joint names, gripper mechanisms and physical approximations are documented by format.

## Availability and permission limits

Reviewed on 2026-10-15.

| Manufacturer / scope | Available source | Catalog scope |
|---|---|---|
| Kawasaki RS and duAro | [Manufacturer ROS repository](https://github.com/Kawasaki-Robotics/khi_robot), [CAD Data Disclaimer](https://kawasakirobotics.com/products/cad-disclaimer/) | The CAD terms distinguish layout/interference use from other copying, modification and distribution. General simulation/training redistribution permission was not established; these meshes are not included. [Details](../models/kawasaki/README.md). |
| NACHI MZ07 | [Nishida-Lab source](https://github.com/Nishida-Lab/nachi_project) | This community source supplies an incomplete license declaration and no clear mesh redistribution scope. [Details](../models/nachi/README.md). |
| JAKA stand-alone A/C/Pro/S/Zu/MiniCobo models | [Manufacturer ROS 2 repository](https://github.com/JAKARobotics/jaka_ros2) | Its description package declares `TODO` as its license. The separately licensed Lumi mobile-manipulator assembly is included. |
| ARX official model depot | [ARX_Model](https://github.com/ARXroboticsX/ARX_Model) | Complete meshes are published without a license in the reviewed depot. The included L5 MJCF has its own Menagerie BSD-3-Clause source and license. |
| Precise Automation PF3400SX | [Manufacturer source](https://github.com/precise-automation/tcs-ros-rviz) | The stated redistribution grant is limited to customers. Permission for this general model collection was not established. |
| ESTUN / CoDroid | [CoDroid downloads](https://www.codroid.ai/en/file), [ESTUN industrial robots](https://www.estun.com/gjxrj/) | The reviewed pages provide CAD/product materials without an identified redistributable runtime model. |
| SIASUN / DUCO | [SIASUN downloads](https://www.siasun.com/download.html), [DUCO development documentation](https://docs.ducorobots.cn/zh/develop/latest/index.html) | The reviewed official sources do not provide an accessible model source with explicit redistribution terms for this catalog. |
| Yamaha | [Manufacturer downloads](https://global.yamaha-motor.com/business/robot/download/) | CAD access is directed to the member site; an openly redistributable runtime model was not identified. |

Some individual variants of included brands also have incomplete upstream resources or licensing: RealMan force-sensor variants, AUBO i7H, Flexiv MICO-Plus, and the Piper camera assembly. Their incomplete files are not catalog entries. Included RealMan and AUBO models use the separately licensed manufacturer sources identified in their READMEs.

## Loading coverage

The model records distinguish file and resource loading from task execution. URDF entries are checked with yourdfpy 0.0.60, including visual/collision geometry and joint configuration updates. MJCF entries are compiled with MuJoCo 3.16.0 and evaluated with `mj_forward`. Checks copy the complete format directory to another location and load by absolute path from a separate working directory.

Some bundled COLLADA assets declare millimetre or inch units. The plain yourdfpy 0.0.60 / trimesh 5.1.1 loader does not apply these unit declarations, so resource loading and joint configuration checks do not establish dimensional accuracy. The affected model READMEs identify this limitation. The [preview renderer](PREVIEWS.md) applies declared units to meshes and file-local transforms; consuming loaders must also honor them.

Dynamic tasks, controller performance, hardware operation and training behavior are outside these loading records. Additional simulators are supported only to the extent stated by the corresponding model's own verification record.
