# Contributing

Contributions help users load complete robot models in their own projects through clear file paths. New models, resource completion, loading fixes, and documentation improvements are welcome. Prioritize platforms used in embodied manipulation research and distinct hardware configurations. Include additional product variants when they provide a concrete use beyond an existing model.

## Prepare the sources

Identify the manufacturer, model, hardware revision, and assembly. Confirm the sources and redistribution permissions of the upstream model and its resources. For each format, record the source URL, tag or commit, upstream file locations, and license files.

Read upstream code and models outside this repository. Reuse an existing local checkout when available; place new reference projects under the workspace's `sources/<project>/` directory. Copy the model and resources to be published into this repository after reviewing and organizing them.

Different formats for the same model may come from different upstream projects. Record their sources and license scopes separately. Include files lacking redistribution permission only after obtaining authorization.

## Organize the files

Follow the [model file specification](docs/MODEL_LAYOUT.md) for entry files, meshes, textures, included files, and licenses. Keep each included format complete, and add a format when its actual files are available.

Inspect resource references and make them local relative references supported by the target loader. Preserve mechanical structure, inertial properties, collisions, and drive relationships. Use clearly named variants for different grippers, hardware revisions, or simulation configurations.

Create `models/<manufacturer>/<model>/README.md` from the [model README template](docs/templates/MODEL_README.md), replacing template fields with actual information in English. Use paths relative to the repository root in the entry table so users can join them with their local checkout path.

Include a MuJoCo-rendered `preview.png` and its `preview.json` rendering record for the model gallery. The [preview documentation](docs/PREVIEWS.md) describes the rendering method and distinguishes native MJCF previews from static URDF visualizations.

## Validate the model

Choose checks that can directly detect problems in the contribution:

| Change | Verification purpose | Action if a problem is found |
|---|---|---|
| New model or format | The native loader reads the entry and resolves all dependencies | Supply missing files or correct the entry, format, or loading options |
| Resource paths or layout | Loading succeeds after relocating the complete model and changing the working directory | Fix absolute paths, missing dependencies, or incorrect relative references |
| Joints, actuators, grippers, or constraints | Affected joints and grippers move as documented | Correct the relevant relationships or physical definitions |
| Documentation | Entries, links, and steps match the current files | Correct the documentation or supply missing files |

Record the actual environment, simulator version, entry, loading parameters, reproducible commands or steps, and results in the model README. Report basic loading and motion results separately. Collect untested environments under Known limitations.

Validate changes to physical behavior in the relevant target environment. Keep verification within the contribution's stated purpose and use the simple scenes needed to establish it.

## Submission contents

A model contribution includes complete resources, sources and licenses, a model README, a preview, and a row in its manufacturer's gallery. The root README files link to manufacturer galleries and list their model counts and formats. Gallery rows include the model or assembly name, preview, native entry links, and model documentation. List only files that actually exist.

Run `python scripts/build_catalog.py` after updating model entry tables. It refreshes manufacturer galleries and both root indexes from those tables while preserving source notes.

Write repository documentation in English. Keep `README.md` as the primary README and update its Simplified Chinese translation, `README_CN.md`, in the same change. The two files must describe the same contents, model entries, examples, and limitations, and link to each other.

Commit descriptions identify the model added or corrected, entry files, behavior changes, and actual verification. When moving an existing model, identify affected paths. Describe the model's current effective differences from upstream in its README.

Published usage documentation belongs in this repository. Keep development plans, research reports, and temporary verification output in the external workspace.
