import os
from google.genai import types

def get_file_info(working_directory, directory=None):
    try:
        abs_workdir_path = os.path.abspath(working_directory)

        if not os.path.isdir(abs_workdir_path):
            return f"Error: '{abs_workdir_path}' is not a directory"
        
        if directory == ".":
            content_dir = os.listdir(abs_workdir_path)
            return datalisting(content_dir, abs_workdir_path)

        if directory not in os.listdir(abs_workdir_path):
            return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"
        
        dir_updated = os.path.join(abs_workdir_path, directory)

        if not os.path.isdir(dir_updated):
            return f"Error: '{directory}' is not a directory"
        
        content_dir = os.listdir(dir_updated)
        return datalisting(content_dir, dir_updated)
      
    except Exception as e:
        print(f'Error: {e}')


def datalisting(content_dir, path):
    data = []
    for f in content_dir:
        filepath = os.path.join(path, f)
        metadata = f'- {f}: file_size={os.stat(filepath).st_size} bytes, is_dir={os.path.isdir(filepath)}'
        data.append(metadata)

    return "\n".join(data)

schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )