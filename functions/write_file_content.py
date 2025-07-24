import os
from google.genai import types

def write_file(working_directory, file_path, content):
    full_working_directory = os.path.abspath(working_directory)
    full_file_path = os.path.join(full_working_directory, file_path)
    file_path_dirs = os.path.dirname(full_file_path)
    
    if not full_file_path.startswith(full_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(file_path_dirs):
        try:
            os.makedirs(file_path_dirs, exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
        
    if os.path.exists(full_file_path) and os.path.isdir(full_file_path):
        return f'Error: "{file_path}" is a directory, not a file'

    try:
        with open(full_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        print(f"Error: Error writing to file: {e}")

schema_write_file_content = types.FunctionDeclaration(
    name="write_file",
    description="- Write or overwrite files, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the python file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file."
            )
        },
        required=["file_path", "content"],
    ),
)