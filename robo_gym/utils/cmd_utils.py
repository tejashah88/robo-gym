from typing import Any
import numpy as np

def construct_roslaunch_command(module: str, launch_file: str, launch_args: dict[str, Any] = {}) -> str:
    """Construct a full roslaunch command to run for simulations from a base command and its arguments.

    Args:
        base_cmd (string): The base roslaunch command containing the module and launch file
        launch_args (float): y coordinate of the point.

    Returns:
        constructed_cmd (string): The fully constructed roslaunch command.

    """

    launch_args_merged = ''
    for (name, value) in launch_args.items():
        if type(value) == bool:
            # roslaunch expects the lowercase version of Python's boolean values
            value = 'true' if value else 'false'
        elif type(value) in [int, float, np.number]:
            # TODO: This is redundant (and will be removed later) but helpful to highlight that numeric conversions are supported
            value = str(value)
        else:
            value = str(value)

        launch_args_merged += f'{name}:={value} '

    constructed_cmd = f'roslaunch {module} {launch_file} {launch_args_merged}'.strip()
    return constructed_cmd
