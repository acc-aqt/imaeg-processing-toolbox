"""Module containing some utility functions."""
import tkinter as tk
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
