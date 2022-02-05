from typing import Tuple
from pathlib import Path
import image_manipulator as img_mani


def main():
    args = img_mani.argparse_setup()

    if args.pixel:
        pixel_art(args.input_path, args.output_path, args.size, args.pixel_count, args.allow_crop)

    if args.get_average:
        get_average_color(args.input_path)

    if args.average:
        create_average_color_image(args.input_path, args.output_path)

    if args.create:
        create_image(args.color, args.size, args.output_path)

    if args.resize:
        resize_image_from_path(args.input_path, args.output_path, args.size)


def pixel_art(
    input_image_path: Path,
    output_image_path: Path,
    pixel_size: Tuple[int, int],
    pixel_count: Tuple[int, int],
    allow_crop: bool,
):
    print(f"Creating pixelated image of image: {input_image_path}...")
    image, px = img_mani.load_image(input_image_path)

    if pixel_size:
        image = img_mani.set_pixels_size(image, image.size, pixel_size, allow_crop)
    else:
        image = img_mani.set_pixel_count(image, image.size, pixel_count, allow_crop)

    image.save(output_image_path)
    print(f"See pixelated image at: {output_image_path}")


def create_average_color_image(
    input_image_path: Path, output_image_path: Path, output_image_size: Tuple[int, int] = (200, 200)
):
    print(f"Creating image with average color of image: {input_image_path}...")
    input_image, input_px = img_mani.load_image(input_image_path)
    average_color = img_mani.get_average_color(input_px, input_image.size)
    # image, px = img_mani.create_image_with_color(average_color, (200, 200))
    # image.save(output_image_path)
    create_image(average_color, output_image_size, output_image_path)
    print(f"See average color image at: {output_image_path}")
    print(f"Average color of image is: {average_color}")


def get_average_color(input_image_path: Path):
    print(f"Calculating average color of image {input_image_path}...")
    image, px = img_mani.load_image(input_image_path)
    average_color = img_mani.get_average_color(px, image.size)
    print(f"Average color of image is: {average_color}")


def create_image(color: str, size: Tuple, output_path: str):
    image, px = img_mani.create_image_with_color(color, size)
    image.save(output_path)


def resize_image_from_path(input_path: str, output_path: str, size: Tuple):
    img = img_mani.resize_image_from_path(input_path, size)
    img.save(output_path)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess cancelled - Keyboard interrupted")