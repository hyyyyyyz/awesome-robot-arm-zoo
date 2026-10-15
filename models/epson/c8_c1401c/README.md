# Epson C8-C1401C

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Epson C8-C1401C model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

Epson C8-C1401C, 6-joint robot body, with no gripper. The model is supplied by the manufacturer's GitHub organization for use as a robot description in an existing scene.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot body, no gripper | URDF | [`models/epson/c8_c1401c/urdf/c8_c1401c.urdf`](urdf/c8_c1401c.urdf) | Native URDF loader; resolve resources relative to the entry file; use a fixed base for dynamics. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | C8-C1401C; upstream robot body; no gripper or attached tool |
| Units | URDF: metres, kilograms, radians, seconds; mesh scale factors remain explicit in the entry |
| Base | `world`; `base_link` is attached by `base_joint` (xyz = `0 0 0` m, rpy = `0 0 0` rad) |
| Arm joint order | `j1_joint` (revolute), `j2_joint` (revolute), `j3_joint` (revolute), `j4_joint` (revolute), `j5_joint` (revolute), `j6_joint` (revolute) |
| Gripper | None |
| End effector / TCP | Terminal link(s): `j6_link`; no separate calibrated TCP is specified |
| Included poses | No named poses are stored in this URDF. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/epson/c8_c1401c/urdf/c8_c1401c.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| URDF definition and companion meshes | [Epson-Robots/epson-robot-ros2](https://github.com/Epson-Robots/epson-robot-ros2) — manufacturer-maintained | `7ead19a7189e052ab7fb49fdc6922f484f893cdd` | [`epson_robot_description/models/C8-C1401C/urdf/epson_robot.urdf.xacro`](https://github.com/Epson-Robots/epson-robot-ros2/blob/7ead19a7189e052ab7fb49fdc6922f484f893cdd/epson_robot_description/models/C8-C1401C/urdf/epson_robot.urdf.xacro); `epson_robot_description/models/C8-C1401C/meshes/` | [Apache-2.0](urdf/LICENSE) |
| Upstream package metadata | Same project | Same commit | `epson_robot_description/package.xml` | [Preserved manifest](urdf/source_package.xml) |

The package license declaration applies to the robot description and accompanying mesh resources. Upstream copyright and author notices are retained in the entry, package metadata and accompanying notice files. This collection preserves those source terms for the included files.

## Model preparation

Static URDF expanded from the upstream Xacro with xacro 2.1.1 using `rb_model:=C8-C1401C`, `use_fake_hardware:=false`, `controller_ip:=`, `controller_port:=`, `client_ip:=`, `client_builtinmsg_port:=`, `client_userdata_port:=`, `send_format:=`, `recv_format:=`, `weight:=`, `inertia:=`, `eccentricity:=`, `security:=`, `ca_cert:=`, `client_cert:=`, `key:=`, `governance:=`, `permissions:=`, `password:=`, `buffer_size:=`, `namespace:=`, `log_level:=`, `initial_positions_file:=/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi项目开发/sources/robot-zoo-upstreams/epson-robot-ros2/epson_robot_description/models/C8-C1401C/config/initial_positions.yaml`. Resource filenames resolve relative to the URDF file. The source mesh hierarchy is retained under `urdf/resources/`. Links, joint transforms, limits, mesh scales, inertial properties and collision definitions retain the upstream values.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/epson/c8_c1401c/urdf/c8_c1401c.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

- The upstream model omits inertial definitions for 7 geometry-bearing link(s); dynamics engines may supply their own defaults.
- Robot controllers, hardware drivers, calibrated tools and simulator-specific actuation are configured by the consuming project. Other simulator environments have not been tested.
