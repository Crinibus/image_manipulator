from typing import Tuple
from PIL import Image
from PIL.PyAccess import PyAccess

from image_manipulator.misc import RgbColor, iterate_pixels


def get_average_color(pixels, image_size: Tuple[int, int]) -> Tuple[int, int, int]:
    image_width, image_height = image_size
    pixel_count = 0
    image_color = RgbColor()

    for x, y in iterate_pixels(image_width, image_height):
        pixel = pixels[x, y]

        # skip pixels that are transparent
        if pixel[3] == 0:
            continue

        pixel_count += 1
        image_color.add_rgb(pixel)

    image_color.calculate_average(pixel_count)
    return image_color.average_hex


def create_image_with_color(color: Tuple[int, int, int], image_size: Tuple[int, int]) -> Tuple[Image.Image, PyAccess]:
    new_image = Image.new("RGBA", image_size, color)
    pixels = new_image.load()
    return new_image, pixels
