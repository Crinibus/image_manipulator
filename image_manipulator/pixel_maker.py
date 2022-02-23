from typing import Tuple
from PIL import Image
import math

from image_manipulator.resize import crop_image
from image_manipulator.misc import RgbColor, Size


def main():
    input_image_name = input("Enter name of input image\n>")
    image = Image.open(input_image_name)
    pixels = image.load()
    # pixels, image_size = load_image(input_image_name)
    print(f"Size of input image: {image.size}")

    pixel_size_input = input('Enter size of a pixel "width,height"\n>')
    pixel_size_list = pixel_size_input.split(",")
    pixel_size = Size(int(pixel_size_list[0]), int(pixel_size_list[1]))

    pixel_count_width = math.floor(image.size[0] / pixel_size.width)
    pixel_count_height = math.floor(image.size[1] / pixel_size.height)

    num_pixels = pixel_size.width * pixel_size.height

    for x_count in range(pixel_count_width):
        for y_count in range(pixel_count_height):

            image_color = RgbColor()

            for x_pixel in range(pixel_size.width):
                for y_pixel in range(pixel_size.height):
                    pixel = pixels[
                        x_pixel + x_count * pixel_size.width,
                        y_pixel + y_count * pixel_size.height,
                    ]
                    image_color.add_rgb(pixel)

            image_color.calculate_average(num_pixels)

            for x_pixel in range(pixel_size.width):
                for y_pixel in range(pixel_size.height):
                    pixels[
                        x_pixel + x_count * pixel_size.width,
                        y_pixel + y_count * pixel_size.height,
                    ] = image_color.average

    output_path = "output/average_pixel.png"
    image.save(f"{output_path}")
    print(f"\nSee result in {output_path}")


def set_pixels_size(pixels, image_size: Tuple[int, int], pixel_size: Tuple[int, int], allow_crop: bool) -> Image:
    pixel_count_width = math.floor(image_size[0] / pixel_size[0])
    pixel_count_height = math.floor(image_size[1] / pixel_size[1])

    pixels_to_average = pixel_size[0] * pixel_size[1]

    # pixelate(pixels, pixel_size[0], pixel_size[1], pixels_to_average, pixel_count_width, pixel_count_height)
    return pixelate(pixels, pixel_size[0], pixel_size[1], image_size, allow_crop)

    # for x_count in range(pixel_count_width):
    #     for y_count in range(pixel_count_height):

    #         image_color = RgbColor()

    #         for x_pixel in range(pixel_size[0]):
    #             for y_pixel in range(pixel_size[1]):
    #                 pixel = pixels[
    #                     x_pixel + x_count * pixel_size[0],
    #                     y_pixel + y_count * pixel_size[1],
    #                 ]
    #                 image_color.add_rgb(pixel)

    #         image_color.calculate_average(pixels_to_average)

    #         # set pixels to average color
    #         for x_pixel in range(pixel_size[0]):
    #             for y_pixel in range(pixel_size[1]):
    #                 pixels[
    #                     x_pixel + x_count * pixel_size[0],
    #                     y_pixel + y_count * pixel_size[1],
    #                 ] = image_color.average


def set_pixel_count(image: Image, image_size: Tuple[int, int], pixel_count: Tuple[int, int], allow_crop: bool) -> Image:
    pixel_width = math.floor(image_size[0] / pixel_count[0])
    pixel_height = math.floor(image_size[1] / pixel_count[1])

    # pixelate(pixels, pixel_width, pixel_height, pixels_to_average, pixel_count[0], pixel_count[1])
    return pixelate(image, pixel_width, pixel_height, image_size, allow_crop)


def pixelate(image: Image, pixel_width: int, pixel_height: int, image_size: Tuple[int, int], allow_crop: bool):
    pixels = image.load()
    pixels_to_average = pixel_width * pixel_height

    pixel_count_width = image_size[0] // pixel_width
    pixel_count_height = image_size[1] // pixel_height

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

    if image.size[0] > pixelated_size[0] or image.size[1] > pixelated_size[1]:
        if allow_crop:
            print(f"Cropping image from resolution {image.size} to {pixelated_size}...")
            image = crop_image(image, (0, 0), pixelated_size)
        else:
            print("Pixelated area does not cover whole image, if this is not desired use flag --allow-crop to crop image")

    return image


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard cancelled")
