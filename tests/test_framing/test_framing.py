"""Testcases for resizing.py go here."""

import os
from src.framing.framing import add_frame, Colors

current_module_path = os.path.dirname(__file__)
example_image = os.path.join(current_module_path, "../example_image.jpg")


def test_add_frame():
    """Testcase for add_frame()."""
    result_file = os.path.join(current_module_path, "result_white_background_resized_2MP.jpg")

    add_frame(
        input_path=example_image,
        output_path=result_file,
        frame_color=Colors.WHITE,
        frame_scaling_factor=0.05,
        frame_aspect_ratio=1 / 1,
        target_megapixels=2.0,
    )

    os.remove(result_file)
