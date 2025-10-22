import os
import config

def get_files_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_path):
        return f'Error: "{file_path}" is not a file'
    
    with open(abs_path, "r") as file:
        file_content = file.read(config.MAX_CHARACTERS)
    
    if len(file_content) == config.MAX_CHARACTERS:
        file_content += f'[...File "{file_path}" truncated at {config.MAX_CHARACTERS} characters]'
    
    return file_content