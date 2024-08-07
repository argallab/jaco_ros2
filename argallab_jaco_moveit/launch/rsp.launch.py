from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_rsp_launch

# rsp === robot state publisher


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder(
        "argallab_jaco", package_name="argallab_jaco_moveit"
    ).to_moveit_configs()
    return generate_rsp_launch(moveit_config)
