<h1 align="center">Awesome Robot Arm Zoo</h1>

<p align="center">
  <strong>为你的具身智能项目，找一款机械臂。</strong><br>
  面向 VLA、模仿学习和仿真的单臂、双臂与移动操作机器人。按品牌或开源项目浏览，选择适合自己仿真环境的模型。
</p>

<p align="center">
  <a href="#模型目录"><img src="https://img.shields.io/badge/Models-67-0F766E?style=flat-square" alt="67 models"></a>
  <a href="#模型目录"><img src="https://img.shields.io/badge/Brands-32-334155?style=flat-square" alt="32 brands"></a>
  <img src="https://img.shields.io/badge/URDF-70-2563EB?style=flat-square" alt="70 URDF files">
  <img src="https://img.shields.io/badge/MJCF-54-D97706?style=flat-square" alt="54 MJCF files">
  <img src="https://img.shields.io/badge/USD-1-7C3AED?style=flat-square" alt="1 USD file">
</p>

<p align="center">
  <a href="README.md">English</a> · <b>简体中文</b><br>
  <a href="#快速开始">快速开始</a> · <a href="#模型目录">浏览模型</a> · <a href="#接入你的项目">接入项目</a> · <a href="#参与贡献">参与贡献</a>
</p>

<table align="center">
  <tr>
    <td align="center" width="33%">
      <a href="models/franka/panda/README.md"><img src="models/franka/panda/preview.png" width="240" alt="Franka Panda"><br><b>Franka Panda</b></a>
      <br><sub>URDF · MJCF</sub>
    </td>
    <td align="center" width="33%">
      <a href="models/agilex/piper/README.md"><img src="models/agilex/piper/preview.png" width="240" alt="AgileX PiPER"><br><b>AgileX PiPER</b></a>
      <br><sub>URDF · MJCF</sub>
    </td>
    <td align="center" width="33%">
      <a href="models/the_robot_studio/so101/README.md"><img src="models/the_robot_studio/so101/preview.png" width="240" alt="SO-101"><br><b>SO-101</b></a>
      <br><sub>URDF · MJCF</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="models/enactic/openarm_v2_dual/README.md"><img src="models/enactic/openarm_v2_dual/preview.png" width="240" alt="OpenArm v2 dual"><br><b>OpenArm v2 dual</b></a>
      <br><sub>URDF · MJCF</sub>
    </td>
    <td align="center" width="33%">
      <a href="models/galaxea/r1_lite_2025/README.md"><img src="models/galaxea/r1_lite_2025/preview.png" width="240" alt="Galaxea R1 Lite"><br><b>Galaxea R1 Lite</b></a>
      <br><sub>URDF</sub>
    </td>
    <td align="center" width="33%">
      <a href="models/trossen/aloha2/README.md"><img src="models/trossen/aloha2/preview.png" width="240" alt="Trossen ALOHA 2"><br><b>Trossen ALOHA 2</b></a>
      <br><sub>MJCF</sub>
    </td>
  </tr>
</table>

<p align="center"><sub>点击图片查看模型文件、配置变体和使用说明。<a href="docs/PREVIEWS.md">了解预览图</a></sub></p>

## 快速开始

先在 MuJoCo 中打开一个 Panda 场景：

```sh
git clone --depth 1 https://github.com/hyyyyyyz/awesome-robot-arm-zoo.git
cd awesome-robot-arm-zoo
python -m pip install mujoco
```

完整模型文件在克隆后约占 **1.8 GB** 磁盘空间。

在仓库根目录运行下面的 Python 代码：

```python
from pathlib import Path

import mujoco
import mujoco.viewer

scene = Path("models/franka/panda/mjcf/menagerie/scene.xml").resolve()
model = mujoco.MjModel.from_xml_path(str(scene))
mujoco.viewer.launch(model)
```

这会打开带地板和灯光的 Panda 场景。在自己的 MuJoCo 场景中使用机器人时，选择同目录下的 [`panda.xml`](models/franka/panda/mjcf/menagerie/panda.xml)。

## 模型目录

**32 个品牌与开源项目，67 个型号与装配。** 点击品牌或项目查看模型图库、可用格式和模型文件。收录以研究平台及有代表性的单臂、双臂和移动操作配置为主。

<!-- MODEL_CATALOG:START -->

| 品牌 / 项目 | 模型数 | 格式 |
|---|---:|---|
| [ABB](models/abb/README.md) | 1 | URDF |
| [AgiBot](models/agibot/README.md) | 1 | USD |
| [AgileX](models/agilex/README.md) | 3 | URDF, MJCF |
| [AIRBOT](models/airbot/README.md) | 2 | MJCF |
| [ARX](models/arx/README.md) | 2 | URDF, MJCF |
| [AUBO](models/aubo/README.md) | 1 | URDF |
| [DENSO](models/denso/README.md) | 1 | URDF |
| [Dobot](models/dobot/README.md) | 1 | URDF |
| [Elephant Robotics](models/elephant_robotics/README.md) | 2 | URDF |
| [Enactic](models/enactic/README.md) | 2 | URDF, MJCF |
| [FANUC](models/fanuc/README.md) | 1 | URDF |
| [Flexiv](models/flexiv/README.md) | 3 | URDF, MJCF |
| [Franka Robotics](models/franka/README.md) | 5 | URDF, MJCF |
| [Galaxea](models/galaxea/README.md) | 2 | URDF |
| [JAKA](models/jaka/README.md) | 1 | URDF |
| [Kinova](models/kinova/README.md) | 4 | URDF, MJCF |
| [Koch](models/koch/README.md) | 1 | MJCF |
| [KUKA](models/kuka/README.md) | 1 | URDF, MJCF |
| [Lebai](models/lebai/README.md) | 2 | URDF |
| [LeKiwi](models/lekiwi/README.md) | 1 | URDF |
| [Pollen Robotics](models/pollen_robotics/README.md) | 2 | URDF, MJCF |
| [RealMan](models/realman/README.md) | 3 | URDF |
| [Rethink Robotics](models/rethink_robotics/README.md) | 2 | URDF, MJCF |
| [ROBOTIS](models/robotis/README.md) | 3 | URDF |
| [ROKAE](models/rokae/README.md) | 1 | URDF |
| [Seeed Studio](models/seeed_studio/README.md) | 1 | MJCF |
| [The Robot Studio](models/the_robot_studio/README.md) | 2 | URDF, MJCF |
| [Trossen / Interbotix](models/trossen/README.md) | 5 | URDF, MJCF |
| [UFACTORY](models/ufactory/README.md) | 4 | URDF, MJCF |
| [Unitree](models/unitree/README.md) | 1 | URDF, MJCF |
| [Universal Robots](models/universal_robots/README.md) | 5 | URDF, MJCF |
| [XLeRobot](models/xlerobot/README.md) | 1 | URDF |

<!-- MODEL_CATALOG:END -->

## 接入你的项目

把仓库放在项目的模型资源目录，或你习惯存放资产的位置。在目录里选好机器人，打开型号说明，复制所需格式的模型路径。例如：

| 型号 | 格式 | 相对仓库根目录的文件路径 |
|---|---|---|
| Franka Panda | MJCF | [`models/franka/panda/mjcf/menagerie/panda.xml`](models/franka/panda/mjcf/menagerie/panda.xml) |
| Franka Panda | URDF | [`models/franka/panda/urdf/panda.urdf`](models/franka/panda/urdf/panda.urdf) |
| SO-101 | URDF | [`models/the_robot_studio/so101/urdf/so101_new_calib.urdf`](models/the_robot_studio/so101/urdf/so101_new_calib.urdf) |
| AgiBot G1 | USD | [`models/agibot/g1_120s/usd/robot.usda`](models/agibot/g1_120s/usd/robot.usda) |

将文件路径与你本地的仓库位置拼接，交给项目中已有的模型加载器。**移动模型时，请一起复制完整的 `urdf/`、`mjcf/` 或 `usd/` 目录**，保留配套网格、纹理和引用文件。

### 选哪种格式？

| 你的项目 | 从这里开始 |
|---|---|
| MuJoCo | 选择该型号提供的 MJCF；`scene.xml` 是带演示环境的场景文件 |
| ROS，或支持导入 URDF 的仿真器 | 选择 URDF；夹爪、固定底座和导入选项见型号说明 |
| Isaac Sim / Genie Sim | AgiBot G1 的原生 USD；材质模块和加载要求见型号说明 |

各型号提供的格式不同。具体文件、关节信息和加载示例都在对应的型号 README 中。

## 来源与许可

模型主要来自厂商和开源硬件项目仓库，部分模型来自大学团队和 [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie)。感谢原作者和维护者公开这些资源。

**不同模型、不同格式的许可证可能不同。** 使用或分发模型前，请查看型号 README 中的来源和许可链接；原始许可证及署名文件随模型一起保留。

AgiBot G1 使用 CC BY-NC-SA 4.0，包含非商业和相同方式共享要求；其资源及预览图遵循该许可。

## 已知限制

- 不同型号和格式的仿真器支持情况不同，请先查看型号说明。URDF 和 USD 预览仅展示外观；控制器、动力学和训练效果需要在自己的项目里验证。
- 部分 COLLADA 文件使用毫米或英寸。导入器需要正确读取文件声明的单位，受影响的型号页有具体说明。

已测试的环境和暂未收录的模型见[来源覆盖与加载说明](docs/SOURCE_COVERAGE.md)。

## 参与贡献

这份目录面向 VLA 与具身操作，仍在持续扩充。如果你常用的研究平台或硬件配置还没有收录，欢迎[提 Issue](https://github.com/hyyyyyyz/awesome-robot-arm-zoo/issues) 告诉我们，或直接提交 PR 补充模型。官方模型仓库和下载链接也很有帮助。

也欢迎修复加载问题、补充模型格式，或分享使用示例。提交模型文件时，请注明来源并保留许可证，具体要求见[贡献指南](CONTRIBUTING.md)。
