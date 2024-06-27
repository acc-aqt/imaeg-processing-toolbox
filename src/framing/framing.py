"""An exemplary python module."""

from PIL import Image
from enum import Enum


class Colors(Enum):
    """Enum representing different colors."""

    BLACK = 0
    WHITE = 1


class ImageFramingException(Exception):
    """Custom Exception to raise within the image framing process."""

    pass


def add_frame(
    input_path,
    output_path,
    frame_color=Colors.WHITE,
    frame_scaling_factor=0.05,
    frame_aspect_ratio=1 / 1,
    target_megapixels=2,
    quality=95,
):
    """
    Add a background frame to an image.

    :param input_path: Path to the input image file.
    :param output_path: Path to save the framed image.
    :param frame_color: Color of the background frame.
    :param frame_scaling_factor: Scaling factor for the frame to add on the longer side of the image.
    :param frame_aspect_ratio: Final aspect ratio width/height of the final image, including the background frame.
    :param target_megapixels: Desired image size in megapixels
    :param quality: Value for Quality of resized image. Default set to 95 to keep high quality.
    """
    # Calculate target number of pixels
    target_pixels = target_megapixels * 1_000_000

    with Image.open(input_path) as img:
        image_width = img.width
        image_height = img.height
        if image_height > image_width:
            frame_height = int(image_height * (1 + frame_scaling_factor))
            frame_width = int(frame_aspect_ratio * frame_height)
        else:
            frame_width = int(image_width * (1 + frame_scaling_factor))
            frame_height = int(frame_width / frame_aspect_ratio)

        if frame_color == Colors.WHITE:
            background_color_tuple = (255, 255, 255)
        elif frame_color == Colors.BLACK:
            background_color_tuple = (0, 0, 0)
        else:
            raise ImageFramingException("Background Color not yet implemented!")

        img_framed = Image.new("RGB", (frame_width, frame_height), background_color_tuple)

        offset_x = int((frame_width - image_width) / 2)
        offset_y = int((frame_height - image_height) / 2)
        img_framed.paste(img, (offset_x, offset_y))  # , mask = image)

        # Get current dimensions and number of pixels
        current_pixels = frame_width * frame_height

        # Calculate scaling factor
        scale_factor = (target_pixels / current_pixels) ** 0.5

        # Calculate new dimensions
        new_width = int(frame_width * scale_factor)
        new_height = int(frame_height * scale_factor)

        # Resize image
        resized_img = img_framed.resize((new_width, new_height))
        resized_img.save(output_path, quality=quality)

        print(f"Wrote image '{output_path}'!")
        print(f"New dimensions: {new_width}x{new_height} ({target_megapixels:.2f} MP)")
