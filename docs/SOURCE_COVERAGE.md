# Source coverage

This collection contains model files from 32 brands and open-source hardware projects. Manufacturer and hardware-project descriptions are prioritized; ROS-Industrial, university, community and Google DeepMind Menagerie sources are identified separately in each model's source table. Sources are pinned to the upstream commits recorded in the model READMEs.

Each model directory lists its actual hardware or assembly, file entries, resource scope and applicable licenses. A manufacturer's presence in the catalog identifies the included models, rather than its entire product range.

## Source families

| Source | Included scope | Source records |
|---|---|---|
| Manufacturer and hardware-project repositories | Prepared static URDFs and their referenced visual/collision resources; existing native files where supplied | Brand and model READMEs |
| Örebro University | ABB YuMi dual-arm description | [YuMi model notes](../models/abb/yumi_irb14000/README.md) |
| Stanford ARX SDK | X5 URDF and meshes | [X5 model notes](../models/arx/x5/README.md) |
| Community Koch v1.1 model | Version-matched MJCF and meshes with their component license | [Koch v1.1 model notes](../models/koch/koch_v1_1/README.md) |
| Google DeepMind MuJoCo Menagerie | Selected MJCF robot assemblies and separate demonstration scenes | Each included model's README and format notes |

The same hardware may have independently sourced URDF and MJCF definitions. Their joint names, gripper mechanisms and physical approximations are documented by format.

## Availability and permission limits

Reviewed on 2026-10-16.

| Manufacturer / scope | Available source | Catalog scope |
|---|---|---|
| Kawasaki RS and duAro | [Manufacturer ROS repository](https://github.com/Kawasaki-Robotics/khi_robot), [CAD Data Disclaimer](https://kawasakirobotics.com/products/cad-disclaimer/) | The CAD terms distinguish layout/interference use from other copying, modification and distribution. General simulation/training redistribution permission was not established; these meshes are not included. [Details](../models/kawasaki/README.md). |
| NACHI MZ07 | [Nishida-Lab source](https://github.com/Nishida-Lab/nachi_project) | This community source supplies an incomplete license declaration and no clear mesh redistribution scope. [Details](../models/nachi/README.md). |
| JAKA stand-alone A/C/Pro/S/Zu/MiniCobo models | [Manufacturer ROS 2 repository](https://github.com/JAKARobotics/jaka_ros2) | Its description package declares `TODO` as its license. The separately licensed Lumi mobile-manipulator assembly is included. |
| ARX official model depot | [ARX_Model](https://github.com/ARXroboticsX/ARX_Model) | Complete meshes are published without a license in the reviewed depot. The included L5 MJCF has its own Menagerie BSD-3-Clause license; the X5 URDF and meshes come from Stanford's MIT-licensed SDK. R5 meshes in ARX_Model remain outside the catalog, and the separate BSD-licensed R5 SDK does not contain their mesh dependencies. |
| Precise Automation PF3400SX | [Manufacturer source](https://github.com/precise-automation/tcs-ros-rviz) | The stated redistribution grant is limited to customers. Permission for this general model collection was not established. |
| ESTUN / CoDroid | [CoDroid downloads](https://www.codroid.ai/en/file), [ESTUN industrial robots](https://www.estun.com/gjxrj/) | The reviewed pages provide CAD/product materials without an identified redistributable runtime model. |
| SIASUN / DUCO | [SIASUN downloads](https://www.siasun.com/download.html), [DUCO development documentation](https://docs.ducorobots.cn/zh/develop/latest/index.html) | The reviewed official sources do not provide an accessible model source with explicit redistribution terms for this catalog. |
| Yamaha | [Manufacturer downloads](https://global.yamaha-motor.com/business/robot/download/) | CAD access is directed to the member site; an openly redistributable runtime model was not identified. |
| Dobot X-Trainer USD | [Official simulation project](https://github.com/embodied-dobot/x-trainer), [referenced asset download](https://huggingface.co/dstx123/xtrainer-leisaac) | The external USD asset repository has no license declaration in the reviewed revision. The simulation code's license does not establish the USD resources' redistribution terms. |

Some individual variants of included brands also have incomplete upstream resources or licensing: AUBO i7H, Flexiv MICO-Plus, and the Piper camera assembly. Their incomplete files are not catalog entries. The RM75-6F force-sensor arm is included from the manufacturer's model repository. Included RealMan and AUBO models use the separately licensed manufacturer sources identified in their READMEs.

## Loading coverage

The model records distinguish file and resource loading from task execution. URDF entries are checked with yourdfpy 0.0.60, including visual/collision geometry and joint configuration updates. MJCF entries are compiled with MuJoCo 3.16.0 and evaluated with `mj_forward`. The AgiBot G1 native USD is checked with OpenUSD 0.26.8 for layer composition, instance meshes, relationship targets and finite geometry. Its OmniPBR MDL module is supplied by Isaac Sim; Isaac Sim physics, sensors and MDL execution have not been tested.

Checks copy the complete format directory to another location and load by absolute path from a separate working directory.

Some bundled COLLADA assets declare millimetre or inch units. The plain yourdfpy 0.0.60 / trimesh 5.1.1 loader does not apply these unit declarations, so resource loading and joint configuration checks do not establish dimensional accuracy. The affected model READMEs identify this limitation. The [preview renderer](PREVIEWS.md) applies declared units to meshes and file-local transforms; consuming loaders must also honor them.

Dynamic tasks, controller performance, hardware operation and training behavior are outside these loading records. Additional simulators are supported only to the extent stated by the corresponding model's own verification record.
