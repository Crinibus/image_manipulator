from .misc import load_image
from typing import Tuple
from PIL import Image


def resize_image(image_path: str, size: Tuple):
    img, px = load_image(image_path)
    resized_img = img.resize(size, Image.ANTIALIAS)
    return resized_img
