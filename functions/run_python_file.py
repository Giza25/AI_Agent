import os
from subprocess import run

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        cmd = ['python3', abs_path]
        if args:
            cmd.extend(args if isinstance(args, list) else [args])
        completed_process = run(cmd, timeout=30, capture_output=True, text=True, cwd=working_directory)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    result = str()
    if completed_process.returncode != 0:
        result += f'\nProcess executed with code {completed_process.returncode}\n'
    if completed_process.stdout:
        result += f'STDOUT:\n{completed_process.stdout}\n'
    else:
        result += f'No output produced\n'
    if completed_process.stderr:
        result += f'STDERR:\n{completed_process.stderr}\n'
    else:
        result += f'No errors produced\n'
    
    return result