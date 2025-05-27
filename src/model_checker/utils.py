#!/bin/python

import subprocess
import os 
from errors import *

def convert_modest_to_python(input_dir: str, modest_path: str):
    """
    Converts Modest models to Python code using the Modest Toolset CLI

    Args:
        input_dir: Path to the modest model
        modest_path: Path to the modest executable
    """
    try:
        # Verify executable permissions
        if not os.path.exists(modest_path):
            raise FileNotFoundError(f"Modest executable not found at {modest_path}")
            
        if not os.path.exists(input_dir):
            raise NotADirectoryError(f"Input directory {input_dir} not found")

        # Build conversion command
        cmd = [
            modest_path,
            "export-to-python",
            input_dir,
            "--output",
            "src/model_checker/modest/modest.py"
        ]

        # Execute conversion
        result = subprocess.run(
            cmd,
            check=True,
            text=True,
            capture_output=True
        )
        
        print(f"Successfully converted models:\n{result.stdout}")
    except Exception as e:
        raise ConversionError(str(e))

def delete_file(file_path):
    """
    Delete a file
    """
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted successfully.")
    except Exception as e:
        raise DeletionError(str(e))

def cleanup():
    """
    Delete intermediate files
    """
    delete_file("src/model_checker/modest/modest.py")
