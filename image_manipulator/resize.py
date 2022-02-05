from typing import Tuple
from PIL import Image

from image_manipulator.misc import load_image


def resize_image_from_path(image_path: str, size: Tuple[int, int]):
    img, px = load_image(image_path)
    resized_img = img.resize(size, Image.ANTIALIAS)
    return resized_img


def resize_image(image: Image, size: Tuple[int, int]):
    resized_img = image.resize(size, Image.ANTIALIAS)
    return resized_img


def crop_image(image: Image, upper_left_corner_pos: Tuple[int, int], new_size: Tuple[int, int]):
    cropped_image = image.crop((upper_left_corner_pos[0], upper_left_corner_pos[1], new_size[0], new_size[1]))
    return cropped_image
