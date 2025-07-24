import os
from os.path import getsize, abspath, join, isfile
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    if not working_directory:
        return 'Error: missing 1 required positional argument: "working_directory"'
    if not file_path:
        return 'Error: missing 1 required positional argument: "file_path"'
    
    full_working_directory = abspath(working_directory)
    full_file_path = join(full_working_directory, file_path)
    
    if not full_file_path.startswith(full_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not isfile(full_file_path):
        return f'Error: File not found or is not a regular file: "{full_file_path}"'
    try:
        with open(full_file_path, mode='r') as f:
            read_data = f.read(MAX_CHARS)
            if getsize(full_file_path) > MAX_CHARS:
                read_data += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            
        return read_data
    except Exception as e:
        return f"Error reading files: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the contents of file up to 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to pull content from, relative to the working directory.",
            ),
        },
    ),
)


# print(get_file_content("calculator", "lorem.txt"))