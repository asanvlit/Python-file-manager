from service import pwd, cd, touch, cat, print_dir_files_names, rm

COMMANDS_DICT = {
    "pwd": lambda x: pwd(),
    "cd": lambda params: cd(params),
    "touch": lambda params: touch(params),
    "cat": lambda params: cat(params),
    "ls": lambda params: print_dir_files_names(params),
    "rm": lambda params: rm(params)
}
