# Awesome-Robot-Arm-Zoo

[English](README.md) | **简体中文**

面向仿真与训练项目的机器人模型文件仓库。每个收录模型随附完整资源，使用者 clone 仓库后，找到对应入口，把本地文件路径填入项目原有的模型加载代码。

**clone → 选择模型与格式 → 复制入口路径 → 使用仿真器原生接口加载。**

## 模型目录

收录 **31 个品牌、482 个型号或装配、541 个入口**，包含 505 个 URDF 与 36 个 MJCF 入口。来源、许可、装配和加载记录见各型号说明。

点击品牌进入模型图库。每行包含标注型号的 MuJoCo 预览图、模型说明和可直接使用的原生入口文件链接。详见[渲染方式](docs/PREVIEWS.md)。

| 品牌图库 | 型号 / 装配数 | 格式 |
|---|---:|---|
| [ABB](models/abb/README.md) | 27 | URDF |
| [AgileX](models/agilex/README.md) | 3 | URDF, MJCF |
| [ARX](models/arx/README.md) | 1 | MJCF |
| [AUBO](models/aubo/README.md) | 11 | URDF |
| [Comau](models/comau/README.md) | 14 | URDF |
| [DENSO](models/denso/README.md) | 3 | URDF |
| [Dobot](models/dobot/README.md) | 10 | URDF |
| [Elephant Robotics](models/elephant_robotics/README.md) | 21 | URDF |
| [Elite Robots](models/elite_robots/README.md) | 5 | URDF |
| [Epson](models/epson/README.md) | 64 | URDF |
| [FANUC](models/fanuc/README.md) | 71 | URDF |
| [Flexiv](models/flexiv/README.md) | 23 | URDF, MJCF |
| [Franka Robotics](models/franka/README.md) | 7 | URDF, MJCF |
| [Han’s / Huayan Robotics](models/hans_robot/README.md) | 6 | URDF |
| [JAKA](models/jaka/README.md) | 1 | URDF |
| [Kinova](models/kinova/README.md) | 17 | URDF, MJCF |
| [KUKA](models/kuka/README.md) | 47 | URDF, MJCF |
| [Lebai](models/lebai/README.md) | 3 | URDF |
| [Mitsubishi Electric](models/mitsubishi/README.md) | 10 | URDF |
| [Pollen Robotics](models/pollen_robotics/README.md) | 1 | URDF |
| [RealMan](models/realman/README.md) | 11 | URDF |
| [Rethink Robotics](models/rethink_robotics/README.md) | 2 | URDF, MJCF |
| [ROBOTIS](models/robotis/README.md) | 6 | URDF |
| [ROKAE](models/rokae/README.md) | 14 | URDF |
| [Stäubli](models/staubli/README.md) | 12 | URDF |
| [Techman Robot](models/techman/README.md) | 10 | URDF |
| [Trossen / Interbotix](models/trossen/README.md) | 10 | URDF |
| [UFACTORY](models/ufactory/README.md) | 7 | URDF, MJCF |
| [Unitree](models/unitree/README.md) | 1 | URDF, MJCF |
| [Universal Robots](models/universal_robots/README.md) | 14 | URDF, MJCF |
| [Yaskawa Motoman](models/yaskawa/README.md) | 50 | URDF |

## 使用方式

克隆仓库到本地：

```sh
git clone https://github.com/hyyyyyyz/awesome-robot-arm-zoo.git
```

在模型目录中选择适合目标环境的格式，并查阅该型号的 README。模型说明会列出相对仓库根目录的入口路径、具体装配、适用环境和必要加载选项。

将入口文件的本地绝对路径填入现有项目。下面使用已收录的 Panda MJCF 入口，路径需替换为本地 checkout 的实际位置：

```python
import mujoco

model = mujoco.MjModel.from_xml_path("/absolute/path/to/awesome-robot-arm-zoo/models/franka/panda/mjcf/menagerie/panda.xml")
```

也可以使用项目自己的路径配置，将模型仓库根目录与入口相对路径拼接。目标项目负责安装其仿真器和相关依赖。

仓库可放在使用项目旁边，也可放在项目自己的依赖目录。模型通过配套的相对资源引用定位网格、纹理和子文件；复制模型到其他位置时，应一起保留其依赖目录。

## 文件组织

模型按厂商、型号和格式组织。以下是目录约定示意：

```text
models/
  <manufacturer>/
    README.md
    <model>/
      README.md
      preview.png
      preview.json
      mjcf/
        <model>.xml
        assets/
        LICENSE
      urdf/
        <model>.urdf
        meshes/
        LICENSE
      usd/
        <model>.usd
        assets/
        LICENSE
```

每个型号只列出实际收录的格式。不同硬件版本、夹爪装配或仿真用途的变体，使用明确的路径区分。机器人本体和包含地板、灯光等内容的展示场景分别标明入口。

完整约定见 [模型文件规范](docs/MODEL_LAYOUT.md)。

## 贡献

欢迎提交具有明确来源和分发许可的机器人模型、资源补全、加载修正及使用说明。

- [贡献指南](CONTRIBUTING.md)：来源、收录步骤、验证和提交内容。
- [模型文件规范](docs/MODEL_LAYOUT.md)：目录、入口、资源引用和变体。
- [单模型 README 模板](docs/templates/MODEL_README.md)：每个型号随附的使用资料。
- [AGENTS.md](AGENTS.md)：仓库维护约定。

厂商官方来源优先；ROS-Industrial、大学维护模型与 Google DeepMind Menagerie 整理模型均在各目录中明确标注。格式子目录中的许可证分别覆盖对应资源，部分网格使用厂商专用条款。

## 使用范围

[来源覆盖与未收录范围](docs/SOURCE_COVERAGE.md)记录来源类别、型号覆盖和许可或资源缺口。

仓库负责提供可定位、资源完整的模型文件和使用说明。关节控制、场景装配、任务定义与训练配置由使用项目管理。

模型是否适用于某个环境，以该模型 README 中记录的入口、加载选项和实际验证版本为准。文件格式可以被导入，并不代表不同仿真器具有相同的控制和物理行为。
