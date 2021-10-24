from typing import Tuple
from pathlib import Path
import image_manipulator as img_mani


def main():
    args = img_mani.argparse_setup()

    if args.pixel_size:
        pixel_art(args.input_path, args.output_path, args.pixel_size)

    if args.average:
        average_color(args.input_path, args.output_path)


def pixel_art(input_image_path: Path, output_image_path: Path, pixel_size: Tuple):
    print(f"Creating pixelated image of image: {input_image_path}...")
    image, px = img_mani.load_image(input_image_path)
    img_mani.set_pixels_average(px, image.size, pixel_size)
    image.save(output_image_path)
    print(f"See pixelated image at: {output_image_path}")


def average_color(input_image_path: Path, output_image_path: Path):
    print(f"Creating image with average color of image: {input_image_path}...")
    input_image, input_px = img_mani.load_image(input_image_path)
    average_color = img_mani.get_average_color(input_px, input_image.size)
    image, px = img_mani.create_image_with_color(average_color, (200, 200))
    image.save(output_image_path)
    print(f"See average color at: {output_image_path}")


if __name__ == "__main__":
    main()
