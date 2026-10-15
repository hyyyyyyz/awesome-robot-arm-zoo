# Awesome-Robot-Arm-Zoo

**English** | [简体中文](README_CN.md)

A repository of robot model files for simulation and training projects. Each included model comes with its complete resources. Clone the repository, find the appropriate entry file, and pass its local path to your project's existing model loader.

**Clone → choose a model and format → copy the entry path → load with your simulator's native API.**

## Models

The repository currently contains contribution guidelines and documentation templates. Model files have not been added yet. Entries will appear here as models are included.

## Usage

Clone the repository:

```sh
git clone https://github.com/hyyyyyyz/awesome-robot-arm-zoo.git
```

Choose a format for your target environment and read the model's README. Each model README lists entry paths relative to the repository root, the specific assembly, supported environments, and required loading options.

Pass the entry file's absolute local path to your existing project. The following example illustrates native MuJoCo loading; replace the path with an actual model file:

```python
import mujoco

model = mujoco.MjModel.from_xml_path("/absolute/path/to/model.xml")
```

You can also use your project's path configuration to join the repository root with a relative entry path. The consuming project installs its simulator and dependencies.

Place this repository beside your project or in its dependency directory. Models locate meshes, textures, and included files through relative resource references. When copying a model elsewhere, keep its dependency directories together.

## Repository layout

Models are organized by manufacturer, model, and format. The following tree illustrates the directory convention:

```text
models/
  <manufacturer>/
    <model>/
      README.md
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

Licenses and source information in each model directory specify the terms for that model and its meshes and textures.

## Scope

The repository provides model files with complete resources, clear paths, and usage documentation. Consuming projects manage joint control, scene assembly, task definitions, and training configuration.

A model's applicability to an environment is determined by the entry file, loading options, and tested versions documented in its README. Importing a file format does not establish equivalent control or physical behavior across simulators.
