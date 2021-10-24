from typing import Tuple
from PIL import Image
from dataclasses import dataclass
from .misc import RgbColor


def main():
    input_image_name = input("Enter name of input image\n>")
    image = Image.open(input_image_name)
    pixels = image.load()
    pixel_count = image.size[0] * image.size[1]
    print("Size of input image:", image.size)

    image_color = RgbColor()

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = pixels[x, y]
            image_color.add_rgb(pixel)

    image_color.calculate_average(pixel_count)

    print(f'\nAverage image color is: {image_color.average}')

    average_color_image = Image.new('RGB', (100, 100), 'black')
    average_image_pixels = average_color_image.load()

    for x in range(average_color_image.size[0]):
        for y in range(average_color_image.size[1]):
            average_image_pixels[x, y] = image_color.average

    output_path = "output/average.png"
    print(f'\nSee average color in image {output_path}')

    average_color_image.save(output_path)


def get_average_color(pixels, image_size: Tuple[int, int]) -> Tuple[int, int, int]:
    pixel_count = image_size[0] * image_size[1]
    image_color = RgbColor()

    for x in range(image_size[0]):
        for y in range(image_size[1]):
            pixel = pixels[x, y]
            image_color.add_rgb(pixel)

    image_color.calculate_average(pixel_count)
    #print(f'\nAverage image color is: {image_color.average}')
    return image_color.average


def create_image_with_color(color: Tuple[int, int, int], image_size: Tuple[int, int]):
    new_image = Image.new('RGB', image_size, color)
    pixels = new_image.load()

    # for x in range(new_image.size[0]):
    #     for y in range(new_image.size[1]):
    #         pixels[x, y] = color

    return new_image, pixels


if __name__ == '__main__':
    main()
