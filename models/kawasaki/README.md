# Kawasaki Robotics models

[Kawasaki-Robotics/khi_robot](https://github.com/Kawasaki-Robotics/khi_robot) is the manufacturer's ROS model source for the RS series and duAro dual-arm robot. The newer [khi_ros2](https://github.com/Kawasaki-Robotics/khi_ros2) is also manufacturer-maintained.

## Included models

No model files are included for this manufacturer.

## Known limitations

The official `khi_robot` source at commit `57200db576c6feb7cea442ff06f27334a520eb7a` distinguishes the BSD software license from the KHI CAD license for mesh data in its [description-package manifests](https://github.com/Kawasaki-Robotics/khi_robot/blob/57200db576c6feb7cea442ff06f27334a520eb7a/khi_rs_description/package.xml). Its [README](https://github.com/Kawasaki-Robotics/khi_robot/blob/57200db576c6feb7cea442ff06f27334a520eb7a/README.md#about-cad-data) applies the CAD disclaimer to the STL meshes. The manufacturer's [CAD Data Disclaimer](https://kawasakirobotics.com/products/cad-disclaimer/) limits the stated purpose to checking robot interference and shape in layout design, with other copying, modification and distribution requiring prior written consent. These terms do not establish permission for this collection's general simulation and training distribution.
