"""Module containing some utility functions."""
import os
import tkinter as tk
from pathlib import Path
from tkinter import filedialog


def select_images():
    """
    Open a file dialog for the user to select image files (JPG and PNG).

    Returns:
        List[str]: A list of file paths selected by the user.
    """
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Define the file types for selection
    file_types = [("Image files", "*.jpg *.jpeg *.png")]

    # Open the file dialog
    file_paths = filedialog.askopenfilenames(title="Select Images", filetypes=file_types)

    return file_paths


def evaluate_target_path(input_file, output_sub_directory, suffix):
    """
    Evaluate the target path for the new images.

    :param input_file: Path to the original input file.
    :param output_sub_directory: Name of the subdirectory in which the result file will be saved.
    If set to None, the result file will be saved in the directory of the input_file
    :param suffix: Filename-suffix for the result image.
    """
    if output_sub_directory:
        target_dir = os.path.join(Path(input_file).parent, output_sub_directory)
        if not os.path.isdir(target_dir):
            os.mkdir(target_dir)
    else:
        target_dir = Path(input_file).parent  # output file goes to same directory like original file

    if not suffix:
        target_filename = Path(input_file).name
    else:
        target_filename = Path(input_file).stem + suffix + Path(input_file).suffix

    target_path = os.path.join(target_dir, target_filename)

    return target_path
