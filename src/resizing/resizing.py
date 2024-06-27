"""An exemplary python module."""

from PIL import Image


class ImageResizeException(Exception):
    """Custom Exception to raise within the image resize process."""

    pass


def resize_image_to_megapixels(input_path, output_path, target_megapixels, quality=95):
    """
    Resizes an image to a specific number of megapixels.

    :param input_path: Path to the input image file.
    :param output_path: Path to save the resized image.
    :param target_megapixels: Desired image size in megapixels
    :param quality: Value for Quality of resized image. Default set to 95 to keep high quality.
    """
    # Calculate target number of pixels
    target_pixels = target_megapixels * 1_000_000

    with Image.open(input_path) as img:
        # Get current dimensions and number of pixels
        width, height = img.size
        current_pixels = width * height

        # Calculate scaling factor
        scale_factor = (target_pixels / current_pixels) ** 0.5

        # Calculate new dimensions
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)

        # Resize image
        resized_img = img.resize((new_width, new_height))
        resized_img.save(output_path, quality=quality)

        print(f"Wrote image '{output_path}'!")
        print(f"Original dimensions: {width}x{height} ({current_pixels / 1_000_000:.2f} MP)")
        print(f"New dimensions: {new_width}x{new_height} ({target_megapixels:.2f} MP)")
