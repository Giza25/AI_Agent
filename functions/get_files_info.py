import os

def get_files_info(working_directory: str, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'
    
    result = f''
    for file_name in os.listdir(abs_path):
        file_path = os.path.join(abs_path, file_name)
        file_size = os.path.getsize(file_path)
        is_dir = os.path.isdir(file_path)

        result += f' - {file_name}: file_size={file_size} bytes, is_dir={is_dir}\n'
    return result