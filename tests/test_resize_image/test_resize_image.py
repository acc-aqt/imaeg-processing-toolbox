"""Testcases for resize_image.py go here."""

import os
from src.resize_image.resize_image import resize_image_to_megapixels

current_module_path = os.path.dirname(__file__)
example_image = os.path.join(current_module_path, "../example_image.jpg")


def test_resize_image_to_megapixels():
    """Testcase for resize_image_to_megapixels()."""
    result_file = os.path.join(current_module_path, "result_resized_2MP.jpg")

    resize_image_to_megapixels(
        input_path=example_image,
        output_path=result_file,
        target_megapixels=2.0,
    )

    os.remove(result_file)
