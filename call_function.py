from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_content import schema_get_content
from functions.writefile import schema_write_file
from functions.run_python import schema_run_python

available_functions= types.Tool(
         function_declarations=[
              schema_get_files_info,
              schema_write_file,
              schema_run_python,
              schema_get_content,
         ]
    )