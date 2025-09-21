import os
from functions.config import MAX_FILE_CHAR_SIZE
from google.genai import types


def get_file_content(working_directory ,file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target_file, "r") as file:
            file_content_string = file.read()
            if len(file_content_string) > MAX_FILE_CHAR_SIZE:
                file_content_string = file_content_string[:MAX_FILE_CHAR_SIZE] + f'[...File ] "{target_file}" truncated at {MAX_FILE_CHAR_SIZE} characters]'
        return file_content_string
    except Exception as e:
        return f'Error: {str(e)}'


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to get the content of, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)