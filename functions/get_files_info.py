import os
from os.path import getsize, isdir, abspath

def get_files_info(working_directory, directory=None):
    working_directory = abspath(working_directory)
    target_directory = os.path.join(working_directory, directory)

    if directory not in os.listdir(working_directory) and directory != '.':
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not isdir(target_directory):
        return f'Error: "{directory}" is not a directory'
    
    os.chdir(target_directory)

    files = os.listdir()

    file_info_list = [f'- {file}: file_size={getsize(abspath(file))} bytes, is_dir={isdir(abspath(file))}' for file in files]

    file_info = "\n".join(file_info_list)

    return file_info

print(get_files_info("calculator", "."))