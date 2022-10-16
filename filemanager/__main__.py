import os
import socket

from console import get_parameters
from data import COMMANDS_DICT
from service import sprt_command_and_params, get_translation

print("Started File manager...")

while True:
    print(os.environ.get('USER', os.environ.get('USERNAME')) + '@' + socket.gethostname(), end=' ')
    input_command = get_parameters()
    command, params = sprt_command_and_params(input_command)
    command_func = get_translation(command, COMMANDS_DICT)

    if command_func is not None:
        try:
            result = command_func(params)
            if result is not None:
                print(result)
        except Exception as e:
            print(getattr(e, 'message', str(e)))
    else:
        print("Unknown command")
