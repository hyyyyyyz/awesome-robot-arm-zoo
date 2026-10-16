<h1 align="center">Awesome Robot Arm Zoo</h1>

<p align="center">
  <strong>Robot arm models for embodied AI projects.</strong><br>
  Single arms, dual arms and mobile manipulators for VLA, imitation learning and simulation. Browse the models, choose a format, and load one in your project.
</p>

<p align="center">
  <a href="#models"><img src="https://img.shields.io/badge/Models-46-0F766E?style=flat-square" alt="46 models"></a>
  <a href="#models"><img src="https://img.shields.io/badge/Brands-23-334155?style=flat-square" alt="23 brands"></a>
  <img src="https://img.shields.io/badge/URDF-52-2563EB?style=flat-square" alt="52 URDF files">
  <img src="https://img.shields.io/badge/MJCF-36-D97706?style=flat-square" alt="36 MJCF files">
</p>

<p align="center">
  <b>English</b> · <a href="README_CN.md">简体中文</a><br>
  <a href="#quick-start">Quick start</a> · <a href="#models">Browse models</a> · <a href="#using-models-in-your-project">Use in your project</a> · <a href="#contributing">Contribute</a>
</p>

<table align="center">
  <tr>
    <td align="center" width="33%">
      <a href="models/franka/panda/README.md"><img src="models/franka/panda/preview.png" width="240" alt="Franka Panda"><br><b>Franka Panda</b></a>
      <br><sub>URDF · MJCF</sub>
    </td>
    <td align="center" width="33%">
      <a href="models/universal_robots/ur5e/README.md"><img src="models/universal_robots/ur5e/preview.png" width="240" alt="Universal Robots UR5e"><br><b>Universal Robots UR5e</b></a>
      <br><sub>URDF · MJCF</sub>
    </td>
    <td align="center" width="33%">
      <a href="models/agilex/piper/README.md"><img src="models/agilex/piper/preview.png" width="240" alt="AgileX PiPER"><br><b>AgileX PiPER</b></a>
      <br><sub>URDF · MJCF</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <a href="models/trossen/vx300s/README.md"><img src="models/trossen/vx300s/preview.png" width="240" alt="Trossen ViperX 300S"><br><b>Trossen ViperX 300S</b></a>
      <br><sub>URDF</sub>
    </td>
    <td align="center" width="33%">
      <a href="models/abb/yumi_irb14000/README.md"><img src="models/abb/yumi_irb14000/preview.png" width="240" alt="ABB YuMi"><br><b>ABB YuMi</b></a>
      <br><sub>URDF</sub>
    </td>
    <td align="center" width="33%">
      <a href="models/franka/fr3_duo/README.md"><img src="models/franka/fr3_duo/preview.png" width="240" alt="Franka FR3 Duo"><br><b>Franka FR3 Duo</b></a>
      <br><sub>URDF</sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Click a robot to see its files, variants and usage notes. <a href="docs/PREVIEWS.md">About the previews</a></sub></p>

## Quick start

Open a Panda scene in MuJoCo:

```sh
git clone --depth 1 https://github.com/hyyyyyyz/awesome-robot-arm-zoo.git
cd awesome-robot-arm-zoo
python -m pip install mujoco
```

The model files occupy about **1.1 GB**.

Run this Python snippet from the repository root:

```python
from pathlib import Path

import mujoco
import mujoco.viewer

scene = Path("models/franka/panda/mjcf/menagerie/scene.xml").resolve()
model = mujoco.MjModel.from_xml_path(str(scene))
mujoco.viewer.launch(model)
```

This opens the Panda with a floor and lighting. To add the robot to your own MuJoCo scene, use [`panda.xml`](models/franka/panda/mjcf/menagerie/panda.xml) in the same directory.

## Models

**46 models and assemblies across 23 brands.** Pick a brand to see its gallery, available formats and model files. The collection focuses on research platforms and representative single-arm, dual-arm and mobile-manipulator configurations.

<!-- MODEL_CATALOG:START -->

| Brand | Models | Formats |
|---|---:|---|
| [ABB](models/abb/README.md) | 1 | URDF |
| [AgileX](models/agilex/README.md) | 1 | URDF, MJCF |
| [ARX](models/arx/README.md) | 1 | MJCF |
| [AUBO](models/aubo/README.md) | 1 | URDF |
| [DENSO](models/denso/README.md) | 1 | URDF |
| [Dobot](models/dobot/README.md) | 1 | URDF |
| [Elephant Robotics](models/elephant_robotics/README.md) | 2 | URDF |
| [FANUC](models/fanuc/README.md) | 1 | URDF |
| [Flexiv](models/flexiv/README.md) | 3 | URDF, MJCF |
| [Franka Robotics](models/franka/README.md) | 5 | URDF, MJCF |
| [JAKA](models/jaka/README.md) | 1 | URDF |
| [Kinova](models/kinova/README.md) | 4 | URDF, MJCF |
| [KUKA](models/kuka/README.md) | 1 | URDF, MJCF |
| [Lebai](models/lebai/README.md) | 2 | URDF |
| [Pollen Robotics](models/pollen_robotics/README.md) | 1 | URDF |
| [RealMan](models/realman/README.md) | 2 | URDF |
| [Rethink Robotics](models/rethink_robotics/README.md) | 2 | URDF, MJCF |
| [ROBOTIS](models/robotis/README.md) | 3 | URDF |
| [ROKAE](models/rokae/README.md) | 1 | URDF |
| [Trossen / Interbotix](models/trossen/README.md) | 2 | URDF |
| [UFACTORY](models/ufactory/README.md) | 4 | URDF, MJCF |
| [Unitree](models/unitree/README.md) | 1 | URDF, MJCF |
| [Universal Robots](models/universal_robots/README.md) | 5 | URDF, MJCF |

<!-- MODEL_CATALOG:END -->

## Using models in your project

Keep this repository wherever you store your project's assets. Find your robot in the catalog, open its README, and copy the path for the format you need. For example:

| Model | Format | File path from the repository root |
|---|---|---|
| Franka Panda | MJCF | [`models/franka/panda/mjcf/menagerie/panda.xml`](models/franka/panda/mjcf/menagerie/panda.xml) |
| Franka Panda | URDF | [`models/franka/panda/urdf/panda.urdf`](models/franka/panda/urdf/panda.urdf) |
| ABB YuMi | URDF | [`models/abb/yumi_irb14000/urdf/yumi_irb14000.urdf`](models/abb/yumi_irb14000/urdf/yumi_irb14000.urdf) |

Join the file path with your local checkout location and pass it to your simulator's model loader. **Keep the meshes, textures and included files together when moving a model**—copy its complete `urdf/` or `mjcf/` directory.

### Which format should I use?

| Your project | Start with |
|---|---|
| MuJoCo | An available MJCF model; `scene.xml` files include a demonstration environment |
| ROS or a simulator with a URDF importer | The model's URDF; check its notes for grippers, fixed-base settings and importer requirements |

Formats vary by model. Each model README lists the exact files, joint information and loading examples.

## Sources and licenses

Models come primarily from manufacturer repositories, with additional descriptions from universities and [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie). Thank you to the authors and maintainers who make these resources available.

**Licenses vary by model and format.** Read the source and license links in the model README before reusing or redistributing its assets. The original license texts and notices are included alongside the files.

## Known limitations

- Simulator support varies by model and format; check the model page for loading requirements. URDF thumbnails are static views of the geometry. Controllers, dynamics and training behavior need validation in your own setup.
- Some COLLADA files use millimetres or inches. Your importer needs to honor the units declared in those files; affected model pages have details.

See [source coverage and loading details](docs/SOURCE_COVERAGE.md) for the tested environments and models still missing from the collection.

## Contributing

This collection focuses on VLA and embodied manipulation and is still growing. If a research platform or hardware configuration you use is missing, [open an issue](https://github.com/hyyyyyyz/awesome-robot-arm-zoo/issues) or send a pull request to add it. Links to official model repositories or downloads are welcome too.

Loading fixes, additional model formats and usage examples are also welcome. Please include the model's source and license when contributing files; see the [contribution guide](CONTRIBUTING.md) for details.
