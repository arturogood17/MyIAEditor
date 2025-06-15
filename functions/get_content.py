import os, sys

def get_file_content(working_directory, file_path):
    current_path = os.getcwd()
    workdir = os.path.join(current_path, working_directory)

    if not os.path.exists(workdir):
        return f'Error: Provided working directory does not exists'
    
    file = os.path.join(workdir, file_path)
    if not os.path.exists(file):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(file, "r") as f:
            max_char = f.read(10000)
        
        if sys.getsizeof(max_char) > 10000:
            return max_char + f'[...File "{file_path}" truncated at 10000 characters]'
        else:
            return max_char

    except Exception as e:
        return f'Error: {e}'