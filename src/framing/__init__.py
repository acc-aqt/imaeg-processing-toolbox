"""Package for adding background frames to images."""
import argparse
from framing.framing import ImageFramingException, add_frame, Colors
from utils.utils import select_images, evaluate_target_path

WHITE = "white"
BLACK = "black"


def frame_images():
    """Let user select images and add a background frame for each image."""
    parser = argparse.ArgumentParser(
        prog="frame_images",
        description="Let user select images and add a background frame for each image.",
    )

    parser.add_argument("--output_sub_directory", required=False, help="Save result images in a separate subdirectory.")
    parser.add_argument("--suffix", required=False, help="Filename-suffix for result images")
    parser.add_argument("--frame_color", choices=[WHITE, BLACK], default=WHITE, help="Color of the background frame.")
    parser.add_argument(
        "--frame_scaling_factor",
        default=0.05,
        help="Scaling factor for the frame to add on the longer side of the image.",
    )
    parser.add_argument(
        "--frame_aspect_ratio",
        default=1 / 1,
        help="Final aspect ratio width/height for the image, including the frame.",
    )
    parser.add_argument("--target_MP", default=2, help="Megapixel of the final image, including the frame.")

    args = parser.parse_args()

    target_MP = float(args.target_MP)
    output_sub_directory = args.output_sub_directory
    suffix = args.suffix
    frame_color = args.frame_color
    frame_scaling_factor = float(args.frame_scaling_factor)
    frame_aspect_ratio = float(args.frame_aspect_ratio)

    if not output_sub_directory and not suffix:
        raise ImageFramingException("Either output_sub_directory or suffix must be specified!")

    input_files = select_images()

    if frame_color == WHITE:
        frame_color_tuple = Colors.WHITE
    elif frame_color == BLACK:
        frame_color_tuple = Colors.BLACK
    else:
        raise ImageFramingException(f"Color '{frame_color}' not supported!")

    for input_file in input_files:
        target_path = evaluate_target_path(input_file, output_sub_directory, suffix)
        add_frame(
            input_path=input_file,
            output_path=target_path,
            frame_color=frame_color_tuple,
            frame_scaling_factor=frame_scaling_factor,
            frame_aspect_ratio=frame_aspect_ratio,
            target_megapixels=target_MP,
        )
