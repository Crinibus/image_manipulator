from typing import Tuple

from image_manipulator.misc import load_image
from image_manipulator.resize import crop_image


def create_grid_image(image_path, grid_size: Tuple[int, int], grid_rgb_color: Tuple[int, int, int], allow_crop: bool):
    image, px = load_image(image_path)
    offset_x = image.size[0] // grid_size[0]
    offset_y = image.size[1] // grid_size[1]

    for x_pixel in range(0, image.size[0]):
        for y_pixel in range(0, image.size[1]):
            # skip upper left corner pixel to avoid line at edge
            if x_pixel == 0 and y_pixel == 0:
                continue
            # avoid lines at edges
            if (x_pixel % offset_x == 0 and x_pixel == 0 and y_pixel % offset_y != 0) or (
                y_pixel % offset_y == 0 and y_pixel == 0 and x_pixel % offset_x != 0
            ):
                continue

            if x_pixel % offset_x == 0 or y_pixel % offset_y == 0:
                px[x_pixel - 1, y_pixel - 1] = grid_rgb_color

    # minus one on each axis because don't want a line at the edges of the image
    nice_grid_image_size = (offset_x * grid_size[0] - 1, offset_y * grid_size[1] - 1)

    # plus one on each axis to compare because minus one before
    if image.size[0] > nice_grid_image_size[0] + 1 or image.size[1] > nice_grid_image_size[1] + 1:
        if allow_crop:
            print(f"Cropping image from resolution {image.size} to {nice_grid_image_size}...")
            image = crop_image(image, (0, 0), nice_grid_image_size)
        else:
            print(
                "The grid does not fit nicely over the whole image, if this is not desired use flag --allow-crop to crop image"
            )
            print(f" - The grid fits nicely if the image's resolution was {nice_grid_image_size}")

    return image
