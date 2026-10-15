# Model File Specification

Public model entries use stable paths and resolve their complete resources within a local checkout. Organize files by manufacturer, model, and format so users can choose the entry appropriate for their environment.

## Directories and naming

```text
models/<manufacturer>/<model>/
  README.md
  preview.png
  preview.json
  <format>/
    <entry-file>
    <resource-directories>/
    LICENSE
```

Use short, stable lowercase English names for manufacturer and model directories, with underscores between words. Format directories use `urdf`, `mjcf`, `usd`, or `sdf`. Preserve upstream filenames, mesh names, and resource hierarchy where practical to keep internal references clear.

Create only directories needed by actual files. When grippers, hardware revisions, or physical configurations require distinct resources, use named variant directories within the format directory:

```text
models/<manufacturer>/<model>/
  README.md
  mjcf/
    <variant>/
      <entry-file>
      assets/
      LICENSE
```

The model README's entry table distinguishes complete assemblies, robot models, and demonstration scenes. Floors, lights, cameras, and other scene elements belong to a demonstration scene's dependencies. List entries for integration into an existing scene separately from demonstration entries.

## Resource references

Resources include meshes, textures, materials, submodels, and all other files referenced directly or indirectly by an entry. Each format or variant directory carries its own dependencies by default and serves as the unit for relocation.

| Format | References to include and verify |
|---|---|
| URDF | Visual and collision meshes, textures, and associated files |
| MJCF | XML includes, meshes, textures, submodels, and compiler resource directory settings |
| USD | Sublayers, references, payloads, materials, textures, and other external dependencies |
| SDF | Meshes, materials, includes, and nested model resource paths |

Write relative references according to the format and target loader's resolution rules. Verify that loading by absolute entry path succeeds after relocating the complete directory and running from another working directory.

URDF models intended for direct file loading provide a static URDF entry. Upstream generation sources such as Xacro may accompany it as supplementary files; users reference the prepared entry directly.

Resolve `package://`, `model://`, and network references through local resources supported by the target loader. For variants intended for ROS packages or a specific resource search mechanism, document required settings and environments alongside their entries.

## Model contents

Preserve the model's existing joint types, motion limits, inertial properties, collision geometry, actuators, and mechanical constraints. When changing these definitions, document the effective differences and their intended use.

The model README supplies the mechanical information users need: exact assembly, units, base name and attachment, arm joint order, gripper relationships, end effector or TCP definition, and any poses included in the model. Use the actual sources and model contents as evidence; collect unconfirmed information under Known limitations.

Runtime joint indices may depend on the loader. Describe interfaces primarily through joint and link names.

## Sources and licensing

Each format or variant preserves its upstream licenses and required copyright notices. When multiple sources make up a model, keep each license and explain which files it covers in the model README.

Source records include the project URL, version identifier, and upstream file paths. For converted formats, also record the input source, conversion tool version, and options affecting model contents.

## Entries and support records

Write entry paths relative to the repository root in the model README and link them to actual files. The catalogs in `README.md` and `README_CN.md` link to manufacturer READMEs. Each manufacturer README contains a preview gallery linking every model's documentation and native entries. Keep the two root catalogs synchronized.

Each model includes `preview.png` and `preview.json`, which records the entry, renderer, pose, and camera used for that preview. See [Model previews](PREVIEWS.md) for the rendering method. Keep model and manufacturer names visible beside gallery images.

Each support record identifies an actual entry, assembly, loading options, and simulator version. Record resource loading and affected joint motion results, with reproducible native commands or minimal examples.

Maintain published paths as a usage interface. When adjusting paths, update entry tables, examples, and resource references together.
