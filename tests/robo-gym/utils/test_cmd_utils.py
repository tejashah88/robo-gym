import pytest
from robo_gym.utils import cmd_utils

# Input command argument definitions
BASIC_ARGS = {}

COMMAND_ARGS_SIMPLE = {
    'string_var1': 'string1',
    'string_var2': 'string2'
}

COMMAND_ARGS_COMPLEX = {
    'string_var': 'string',
    'int_var': 6,
    'float_var': 3.14,
    'bool_var': True,
}

# Expected command string definitions (NOTE: indentation sensitive)
EXP_BASIC_COMMAND = "roslaunch example_module_1 example_launch_1.launch"

EXP_COMMAND_WITH_ARGS_SIMPLE = "roslaunch example_module_2 example_launch_2.launch \
string_var1:=string1 \
string_var2:=string2"

EXP_COMMAND_WITH_ARGS_COMPLEX = "roslaunch example_module_3 example_launch_3.launch \
string_var:=string \
int_var:=6 \
float_var:=3.14 \
bool_var:=true"

### correct_launch_commands ###
test_correct_launch_commands = [
    ('example_module_1', 'example_launch_1.launch', BASIC_ARGS, EXP_BASIC_COMMAND),
    ('example_module_2', 'example_launch_2.launch', COMMAND_ARGS_SIMPLE, EXP_COMMAND_WITH_ARGS_SIMPLE),
    ('example_module_3', 'example_launch_3.launch', COMMAND_ARGS_COMPLEX, EXP_COMMAND_WITH_ARGS_COMPLEX)
]
@pytest.mark.parametrize('module, launch_file, launch_args, expected_result', test_correct_launch_commands)
def test_construct_roslaunch_command(module, launch_file, launch_args, expected_result):
    constructed_cmd = cmd_utils.construct_roslaunch_command(module, launch_file, launch_args)
    assert constructed_cmd == expected_result
