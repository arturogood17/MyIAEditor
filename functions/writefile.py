import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_work_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    try:
        if not abs_file_path.startswith(abs_work_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_file_path):
            writing(abs_file_path, content)
        
        writing(abs_file_path, content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: {e}'
    

def writing(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)

schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Writes to the specified file.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file path to the file, relative to the working directory.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The content that is going to be written in the file.",
                ),
            },
        ),
    )