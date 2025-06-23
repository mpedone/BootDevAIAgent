import os
from os.path import getsize, isdir, abspath, join

def get_files_info(working_directory, directory=None):
    if not working_directory:
        return f'Error: missing 1 required positional argument: "working_directory"'
    if not directory:
        directory = '.'

    full_working_directory = abspath(working_directory)
    target_directory = join(full_working_directory, directory)

    if not os.path.exists(full_working_directory):
        return f'Error: No such file or directory: "{working_directory}"'
    if not isdir(full_working_directory):
        return f'Error: "{working_directory}" is not a directory'

    if directory not in os.listdir(full_working_directory) and directory != '.':
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not isdir(target_directory):
        return f'Error: "{directory}" is not a directory'

    files = os.listdir(target_directory)

    file_info_list = [f'- {file}: file_size={getsize(join(target_directory,file))} bytes, is_dir={isdir(join(target_directory, file))}' for file in files]

    file_info = "\n".join(file_info_list)

    return file_info


# print(get_files_info("calculator", "."))
print(get_files_info(".", "pkg"))