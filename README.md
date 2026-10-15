# Awesome-Robot-Arm-Zoo

**English** | [简体中文](README_CN.md)

A repository of robot model files for simulation and training projects. Each included model comes with its complete resources. Clone the repository, find the appropriate entry file, and pass its local path to your project's existing model loader.

**Clone → choose a model and format → copy the entry path → load with your simulator's native API.**

## Models

**31 manufacturers, 482 models or assemblies, and 541 entry files**: 505 URDF and 36 MJCF entries. Model notes identify the exact assembly, source, license and loading records.

Choose a manufacturer to browse its model gallery. Each row shows a labeled MuJoCo preview, links to the model documentation, and direct native entry files. See the [rendering method](docs/PREVIEWS.md).

| Manufacturer gallery | Models / assemblies | Formats |
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

## Usage

Clone the repository:

```sh
git clone https://github.com/hyyyyyyz/awesome-robot-arm-zoo.git
```

Choose a format for your target environment and read the model's README. Each model README lists entry paths relative to the repository root, the specific assembly, supported environments, and required loading options.

Pass the entry file's absolute local path to your existing project. The following example uses the included Panda MJCF entry; replace the checkout prefix with its actual local path:

```python
import mujoco

model = mujoco.MjModel.from_xml_path("/absolute/path/to/awesome-robot-arm-zoo/models/franka/panda/mjcf/menagerie/panda.xml")
```

You can also use your project's path configuration to join the repository root with a relative entry path. The consuming project installs its simulator and dependencies.

Place this repository beside your project or in its dependency directory. Models locate meshes, textures, and included files through relative resource references. When copying a model elsewhere, keep its dependency directories together.

## Repository layout

Models are organized by manufacturer, model, and format. The following tree illustrates the directory convention:

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

Each model lists only the formats actually included. Distinct hardware revisions, gripper assemblies, and simulation variants use explicit paths. Robot models and demonstration scenes containing floors, lights, or other scene elements have separate entry files.

See the [model file specification](docs/MODEL_LAYOUT.md) for the full convention.

## Contributing

Contributions are welcome for robot models with clear sources and redistribution permissions, missing resources, loading fixes, and documentation.

- [Contribution guide](CONTRIBUTING.md): sources, inclusion steps, validation, and submission contents.
- [Model file specification](docs/MODEL_LAYOUT.md): directories, entry files, resource references, and variants.
- [Model README template](docs/templates/MODEL_README.md): usage information accompanying each model.
- [AGENTS.md](AGENTS.md): repository maintenance conventions.

Manufacturer sources are prioritized. ROS-Industrial, university-maintained and Google DeepMind Menagerie models are identified in their model directories. Format-level licenses cover their respective resources; some manufacturer meshes carry specific usage terms.

## Scope

[Source coverage](docs/SOURCE_COVERAGE.md) records source families, model coverage and permission or resource gaps.

The repository provides model files with complete resources, clear paths, and usage documentation. Consuming projects manage joint control, scene assembly, task definitions, and training configuration.

A model's applicability to an environment is determined by the entry file, loading options, and tested versions documented in its README. Importing a file format does not establish equivalent control or physical behavior across simulators.
