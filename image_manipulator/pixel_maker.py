from typing import Tuple
from PIL import Image
import math

from image_manipulator.resize import crop_image
from image_manipulator.misc import RgbColor, Size


def set_pixels_size(pixels, pixel_size: Tuple[int, int], allow_crop: bool) -> Image:
    return pixelate(pixels, pixel_size[0], pixel_size[1], allow_crop)


def set_pixel_count(image: Image, pixel_count: Tuple[int, int], allow_crop: bool) -> Image:
    pixel_width = math.floor(image.size[0] / pixel_count[0])
    pixel_height = math.floor(image.size[1] / pixel_count[1])

    return pixelate(image, pixel_width, pixel_height, allow_crop)


def pixelate(image: Image, pixel_width: int, pixel_height: int, allow_crop: bool):
    image_width, image_height = image.size
    pixels = image.load()
    pixels_to_average = pixel_width * pixel_height

    pixel_count_width = image_width // pixel_width
    pixel_count_height = image_height // pixel_height

    for x_count in range(0, pixel_count_width):
        for y_count in range(0, pixel_count_height):

            image_color = RgbColor()

            # get average color of pixel
            for x_pixel in range(pixel_width):
                for y_pixel in range(pixel_height):
                    pixel = pixels[
                        x_pixel + x_count * pixel_width,
                        y_pixel + y_count * pixel_height,
                    ]
                    image_color.add_rgb(pixel)

            image_color.calculate_average(pixels_to_average)

            # set pixels to average color
            for x_pixel in range(pixel_width):
                for y_pixel in range(pixel_height):
                    pixels[
                        x_pixel + x_count * pixel_width,
                        y_pixel + y_count * pixel_height,
                    ] = image_color.average

    pixelated_size = (pixel_width * pixel_count_width, pixel_height * pixel_count_height)

    if image_width > pixelated_size[0] or image_height > pixelated_size[1]:
        if allow_crop:
            print(f"Cropping image from resolution {image.size} to {pixelated_size}...")
            image = crop_image(image, (0, 0), pixelated_size)
        else:
            print("Pixelated area does not cover whole image, if this is not desired use flag --allow-crop to crop image")

    return image
