import os, subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_work_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    try:
        if not abs_file_path.startswith(abs_work_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        
        if ".py" not in os.path.splitext(abs_file_path):
            return f'Error: "{file_path}" is not a Python file.'
        
        result= subprocess.run(["python3", abs_file_path], timeout=30,
                            capture_output=True,
                            text=True, 
                            cwd=abs_work_path)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        if result.returncode != 0:
            print("Process exited with code", result.returncode)
        if result.stdout == "" and result.stderr == "":
            print("No output produced.")
    except Exception as e:
        return f"Error: executing Python file: {e}"
    

schema_run_python = types.FunctionDeclaration(
        name="run_python_file",
        description="It runs the python file indicated.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file path to the python file, relative to the working directory.",
                ),
            },
        ),
    )