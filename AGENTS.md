# Repository Maintenance Conventions

## Product goal

This repository stores complete robot model files. After cloning it, users copy a model entry file's local path into an existing project and load it through their simulator's native API.

Complete means that every included model ships with all of its runtime resources. Stable file paths, complete dependencies, and accurate model documentation form the public interface.

The default scope covers model files, accompanying resources, usage documentation, and maintenance scripts with a concrete purpose. Consuming projects own scene execution, controllers, and training logic.

## Change boundaries

- Keep the task focused. Prioritize the current model's inclusion, loading, or path issue, and use actual inputs and supported environments to determine the cases that need handling.
- Follow the existing layout and maintain clear responsibilities. Entry scripts coordinate calls; organize substantial maintenance logic by function.
- Document the current delivered state. The model catalog, supported environments, and validation results must match actual files and execution records.
- Preserve existing user changes. Review the change scope before committing and include only the files prepared for the current task.

## Model files

- Follow the [model file specification](docs/MODEL_LAYOUT.md), organizing files by manufacturer, model, and format.
- Include actual files and complete dependencies. Public entries must load from a local checkout, with resource references following the relative path rules of the format and loader.
- Preserve native inertial properties, limits, collision definitions, actuators, and constraints. When changing physical parameters, describe the resulting definitions and their intended use.
- Identify robot models, complete assemblies, and demonstration scenes separately. Use explicit variant paths for meaningful differences in hardware, grippers, or physical configuration.
- Keep published entry paths stable. When a move or rename is necessary, update model documentation, both root README catalogs, and internal references together, and identify affected entries in the commit description.
- Maintain a README for each model using the [template](docs/templates/MODEL_README.md). Include sources, entries, mechanical information, and loading records. Keep template placeholders confined to template files.

## Sources and licensing

- Include models with clear sources, versions, and redistribution permissions. Verify the applicable terms for models, meshes, textures, and other accompanying resources.
- Preserve upstream licenses, copyright notices, and required attribution alongside the files. Record the file scope covered by each source.
- Identify upstream versions with a tag or existing commit identifier. Add digests, checksums, or fingerprints only when they avoid a materially more expensive operation and change what happens next.
- Read relevant upstream files before drawing on an implementation. Keep reference repositories outside this repository in the local workspace. Reuse existing checkouts; place new references under the workspace's `sources/<project>/` directory.

## Verification

Before running a check, identify the specific failure it can detect and what you would change if it failed.

- For documentation changes, check internal links, file paths, and consistency of descriptions.
- For model additions, confirm resource completeness and load the entry with the native loader in the declared environment.
- For path changes, relocate the complete model and change the caller's working directory to detect references tied to an author's machine or the current directory.
- For joint, gripper, or constraint changes, verify the affected motion against the documented assembly.
- Record the simulator version, entry, loading options, steps, and actual results. List environments that have not been tested under the model's Known limitations section.

After checks pass, run additional verification only for new changes, failures, or unresolved concrete concerns.

## Documentation and commits

The root README files introduce the repository and list actual models. The repository's `docs/` directory contains published usage conventions and templates. Keep development research, designs, plans, and progress records in the local workspace's `docs/` directory outside this repository. Keep reference project materials with their checkouts.

Write repository documentation in plain English. `README.md` is the primary README; maintain `README_CN.md` as its synchronized Simplified Chinese translation. Update both in the same change whenever content, model entries, examples, or links change. Keep reciprocal language links near the top of both files. Other repository documentation and templates use English.

Describe current contents, concrete behavior, and usage. Collect limitations in the relevant Scope or Known limitations section. Commit descriptions state the final changes and relevant verification.
