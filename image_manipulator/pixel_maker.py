from typing import Tuple
from PIL import Image
from math import floor
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

    pixel_count_width = floor(image.size[0] / pixel_size.width)
    pixel_count_height = floor(image.size[1] / pixel_size.height)

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


def set_pixels_average(pixels, image_size: Tuple[int, int], pixel_size: Tuple[int, int]) -> None:
    pixel_count_width = floor(image_size[0] / pixel_size[0])
    pixel_count_height = floor(image_size[1] / pixel_size[1])

    num_pixels = pixel_size[0] * pixel_size[1]

    for x_count in range(pixel_count_width):
        for y_count in range(pixel_count_height):

            image_color = RgbColor()

            for x_pixel in range(pixel_size[0]):
                for y_pixel in range(pixel_size[1]):
                    pixel = pixels[
                        x_pixel + x_count * pixel_size[0],
                        y_pixel + y_count * pixel_size[1],
                    ]
                    image_color.add_rgb(pixel)

            image_color.calculate_average(num_pixels)

            for x_pixel in range(pixel_size[0]):
                for y_pixel in range(pixel_size[1]):
                    pixels[
                        x_pixel + x_count * pixel_size[0],
                        y_pixel + y_count * pixel_size[1],
                    ] = image_color.average


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\Keyboard cancelled")
