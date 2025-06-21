import os
from google.genai import types
from functions.get_files_info import get_file_info
from functions.get_content import get_file_content
from functions.writefile import write_file
from functions.run_python import run_python_file

def call_function(function_call_part, verbose= False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    print(f" - Calling function: {function_call_part.name}")

    functions_dict = {"get_file_content": get_file_content,
                      "get_file_info": get_file_info,
                      "write_file": write_file,
                      "run_python_file": run_python_file,}
    
    function_call_part.args["working_directory"] = "./calculator"

    func_name = function_call_part.name
    if func_name not in functions_dict:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name= func_name,
                    response={"error": f"Unknown function: {func_name}"},
                )
            ],
        )
    
    function_result = functions_dict[func_name](**function_call_part.args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name= func_name,
                response={"result": function_result},
            )
        ],
    )