# Elite Robots CS612

[Manufacturer gallery](../README.md) · [All manufacturers](../../../README.md)

<img src="preview.png" width="480" alt="Elite Robots CS612 model preview">

MuJoCo preview · [Rendering record](preview.json) · [Rendering method](../../../docs/PREVIEWS.md)

CS612 6-joint arm without a gripper. The entry preserves the upstream kinematic, visual, collision, inertial and joint-limit definitions.

## Model entries

Entry paths are relative to the repository root.

| Purpose / assembly | Format | Entry path | Target environment and required loading options |
|---|---|---|---|
| Robot model: CS612 6-joint arm without a gripper | URDF | [`models/elite_robots/cs612/urdf/cs612.urdf`](urdf/cs612.urdf) | A native URDF loader with relative mesh resolution; attach the base to the consuming scene. |

## Mechanical information

| Item | Definition |
|---|---|
| Hardware revision and gripper | CS612 6-joint arm without a gripper |
| Units | Metres, kilograms, radians; revolute joint effort in N·m and prismatic effort in N. Mesh scale attributes remain as supplied upstream. |
| Base | `world`; root of the URDF tree. Any supplied fixed base transform is retained. |
| Arm joint order | `shoulder_pan_joint` → `shoulder_lift_joint` → `elbow_joint` → `wrist_1_joint` → `wrist_2_joint` → `wrist_3_joint` |
| Gripper | No gripper is included. |
| End effector / TCP | `flange`, `tool0`; fixed transforms remain in the entry. |
| Included poses | No named poses are defined by this URDF entry. |

## Loading example

```python
from yourdfpy import URDF

robot = URDF.load(
    '/absolute/path/to/awesome-robot-arm-zoo/models/elite_robots/cs612/urdf/cs612.urdf',
    load_meshes=True, load_collision_meshes=True,
    build_collision_scene_graph=True,
)
```

## Sources and licensing

| Format or file scope | Upstream project | Version | Upstream file path | License file |
|---|---|---|---|---|
| Static URDF and its bundled resources (eli_cs_robot_description) | [https://github.com/Elite-Robots/Elite_Robots_CS_ROS2_Driver](https://github.com/Elite-Robots/Elite_Robots_CS_ROS2_Driver) | `3e9e8ca8c9a56b5a5965d15ba4ddd751addd7c33` | `eli_cs_robot_description/urdf/cs.urdf.xacro`; model mesh paths under the named packages | [LICENSE](urdf/LICENSE) |

Bundled upstream resource directories: `eli_cs_robot_description/meshes/cs612/collision`, `eli_cs_robot_description/meshes/cs612/visual`.

License scope: Apache-2.0 for the eli_cs_robot_description package, including model definitions and mesh resources. The complete upstream license texts and notices accompany this format directory.

## Model preparation

The static entry was expanded with xacro 2.1.1 using cs_type:=cs612, name:=cs612, use_fake_hardware:=true, tf_prefix:=, joint_limit_params:=/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi项目开发/sources/robot-zoo-upstreams/elite_cs_ros2/eli_cs_robot_description/config/cs612/joint_limits.yaml, kinematics_params:=/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi项目开发/sources/robot-zoo-upstreams/elite_cs_ros2/eli_cs_robot_description/config/cs612/default_kinematics.yaml, physical_params:=/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi项目开发/sources/robot-zoo-upstreams/elite_cs_ros2/eli_cs_robot_description/config/cs612/physical_parameters.yaml, visual_params:=/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi项目开发/sources/robot-zoo-upstreams/elite_cs_ros2/eli_cs_robot_description/config/cs612/visual_parameters.yaml, transmission_hw_interface:=, safety_limits:=false, safety_pos_margin:=0.15, safety_k_position:=20, headless_mode:=false, robot_ip:=0.0.0.0, script_filename:=, output_recipe_filename:=, input_recipe_filename:=, local_ip:=0.0.0.0, script_command_port:=50004, reverse_port:=50001, script_sender_port:=50002, trajectory_port:=50003, use_tool_communication:=false, tool_voltage:=0, tool_parity:=0, tool_baud_rate:=115200, tool_stop_bits:=1, tool_tcp_port:=54321, fake_sensor_commands:=false, sim_gazebo:=false, sim_ignition:=false, simulation_controllers:=, initial_positions_file:=/Users/jacksonhuang/Documents/ChatGPT/RoboTakumi项目开发/sources/robot-zoo-upstreams/elite_cs_ros2/eli_cs_robot_description/config/initial_positions.yaml. Resources were copied only when referenced by the entry or by one of its mesh/material files. Resource references are local relative paths. Mesh contents and physical parameters retain the upstream definitions. The manufacturer per-model configuration YAMLs supply the limits, transforms, masses and mesh selection. The upstream fake-hardware option is selected; the world-to-base fixed attachment is retained.

## Loading verification

Checks performed on 2026-10-15. The complete format directory was copied to a temporary location and loaded by absolute path from a separate working directory.

| Entry | Environment and loader version | Verification steps | Result |
|---|---|---|---|
| `models/elite_robots/cs612/urdf/cs612.urdf` | macOS 27.2, arm64, Python 3.12.14; yourdfpy 0.0.60 | Load visual/collision geometry and update the joint configuration. | Passed, including resource relocation. |

## Known limitations

Dynamic task execution, controller performance and training behavior have not been validated.

ROS, Gazebo and physics simulators have not been verified for this entry. Default nominal kinematics are included. Calibration and the ROS 2 controller connection have not been verified.
