import os
def file_reader(full_directory_filename: str) -> str:
    """
    Input just the file name. Try calling it with os.path.dirname(os.path.abspath(__file__)) + "/filename"
    Note: Best for text files, since it reads in "r"/read only mode.
    
    full_directory_filename: the name of the file, including the entire working directory.
    
    return: The data inside the file
    """
    with open(full_directory_filename, "r", encoding = 'utf-8') as file:
        return file.read()
