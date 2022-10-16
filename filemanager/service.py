import os
from pathlib import Path

cur_path = os.getcwd()


def pwd():
    return cur_path


def cd(params):
    if len(params) == 1:
        new_dir = build_files_path(params[0])
        if new_dir.exists() & new_dir.is_dir():
            global cur_path
            cur_path = new_dir
            return cur_path
        else:
            raise ValueError("The specified file doesn't exist or isn't a directory")
    else:
        raise ValueError("Incorrect number of parameters")


def touch(params):
    if len(params) > 0:
        new_files_paths = list(map(build_files_path, params))
        list(map(create_file, new_files_paths))
        return new_files_paths
    else:
        raise ValueError("The file name isn't specified")


def cat(params):
    if len(params) > 0:
        files_paths = list(map(build_files_path, params))
        for f in files_paths:
            if f.exists() & f.is_file():
                with f.open('r') as file:
                    print(file.read())
            else:
                raise ValueError("The specified file doesn't exist or isn't a file")
    else:
        raise ValueError("The file name isn't specified")


def ls(params):
    if len(params) == 0:
        files_in_dir = map(build_files_path, [f for f in os.listdir(cur_path)])
    elif len(params) == 1:
        dir_path = build_files_path(params[0])
        if dir_path.exists() & dir_path.is_dir():
            files_in_dir = map(lambda x: build_files_path(x, str(dir_path)), [f for f in os.listdir(dir_path)])
        else:
            raise ValueError("The specified file doesn't exist or isn't a directory")
    else:
        raise ValueError("The file name isn't specified or more than one file specified")
    return files_in_dir


def rm(params):
    if len(params) > 0:
        files_to_remove = map(build_files_path, params)
        for f in files_to_remove:
            print(f)
            if f.exists() & f.is_file():
                # os.remove(f)
                print()
            else:
                raise ValueError("The specified file doesn't exist or isn't a file")
    else:
        raise ValueError("The file name isn't specified or more than one file specified")


def print_dir_files_names(params):
    files_in_dir = ls(params)
    for f in files_in_dir:
        if f.is_file():
            print(f.name)
        elif f.is_dir():
            print(f"{f.name}\\")


def sprt_command_and_params(input_command):
    separated_input = input_command.split()
    return separated_input[0], separated_input[1:]


def get_translation(key, dictionary):
    if key in dictionary:
        return dictionary[key]
    else:
        return None


def build_files_path(dir_path, parent_path=cur_path):
    if os.path.isabs(dir_path):
        return Path(dir_path).resolve()
    else:
        return Path(os.path.join(parent_path, dir_path)).resolve()


def create_file(file_path):
    if not Path(file_path).exists():
        new_file = open(file_path, 'w')
        new_file.close()
        return new_file
    else:
        raise ValueError(f"Such file <{file_path}> already exists")
