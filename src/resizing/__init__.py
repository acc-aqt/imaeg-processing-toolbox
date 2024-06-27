"""Package for resizing of images."""
import argparse
from resizing.resizing import ImageResizeException, resize_image_to_megapixels
from utils.utils import select_images, evaluate_target_path


def resize_images():
    """Let user select images and do the resizing to a certain number of Megapixels."""
    parser = argparse.ArgumentParser(
        prog="resize_images",
        description="Resize interactively selected images to a certain number of Megapixels",
    )

    parser.add_argument("--target_mp", help="Target size in Megapixels")
    parser.add_argument("--output_sub_directory", required=False, help="Save result images in a separate subdirectory")
    parser.add_argument("--suffix", required=False, help="Filename-suffix for result images")

    args = parser.parse_args()

    target_mp = float(args.target_mp)
    output_sub_directory = args.output_sub_directory
    suffix = args.suffix

    if not output_sub_directory and not suffix:
        raise ImageResizeException("Either output_sub_directory or suffix must be specified!")

    input_files = select_images()

    for input_file in input_files:
        target_path = evaluate_target_path(input_file, output_sub_directory, suffix)
        resize_image_to_megapixels(input_path=input_file, output_path=target_path, target_megapixels=target_mp)
