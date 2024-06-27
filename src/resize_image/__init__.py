"""Package for resizing of images."""
import os.path
import argparse
from pathlib import Path
from resize_image.resize_image import ImageResizeException, resize_image_to_megapixels
from utils.utils import select_images


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

        resize_image_to_megapixels(
            input_path=input_file, output_path=os.path.join(target_dir, target_filename), target_megapixels=target_mp
        )
