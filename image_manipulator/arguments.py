import argparse
import pathlib


def argparse_setup() -> argparse.ArgumentParser.parse_args:
    """Setup and return argparse."""
    parser = argparse.ArgumentParser(description="Image Manipulator by Crinibus")

    parser.add_argument(
        "-in",
        "--input-path",
        help="path to input image to manipulate",
        type=pathlib.Path,
        dest="input_path",
        metavar="PATH",
        # required=True,
    )

    parser.add_argument(
        "-out",
        "--output-path",
        help="path to output image",
        type=pathlib.Path,
        dest="output_path",
        metavar="PATH",
    )

    parser.add_argument(
        "--pixel",
        help="pixelate image, use with --size to set size of each pixel or with --pixel-count to specify how many pixels",
        dest="pixel",
        action="store_true",
    )

    parser.add_argument(
        "--pixel-count",
        help="specify number of vertical and horizontal pixels",
        type=int,
        nargs=2,
        dest="pixel_count",
        metavar=("X", "Y"),
    )

    parser.add_argument(
        "-a",
        "--average",
        help="create new image that that the average color of input image",
        dest="average",
        action="store_true",
    )

    parser.add_argument(
        "--get-average",
        help="get the average color of input image",
        dest="get_average",
        action="store_true",
    )

    parser.add_argument(
        "--create",
        help="create a image of a specified size with --size and color with flag --color",
        dest="create",
        action="store_true",
    )

    parser.add_argument(
        "--resize",
        help="resize an image to specified size with --size",
        dest="resize",
        action="store_true",
    )

    parser.add_argument(
        "--allow-crop",
        help="allow cropping the image if e.g. the pixelated area does not cover whole input image",
        dest="allow_crop",
        action="store_true",
    )

    parser.add_argument(
        "--grid",
        help="draw a grid of given size on top of the given image",
        type=int,
        nargs=2,
        dest="grid",
        metavar=("WIDTH", "HEIGHT"),
    )

    parser.add_argument(
        "--size",
        help="specify size",
        type=int,
        nargs=2,
        dest="size",
        metavar=("WIDTH", "HEIGHT"),
    )

    parser.add_argument(
        "--color",
        help=(
            "specify color, supports RGB, HSL and HSV functions, hexadecimal and common HTML color names. "
            "See Pillow ImageColor module for examples"
        ),
        dest="color",
        type=str,
    )

    return validate_arguments(parser)


def validate_arguments(parser: argparse.ArgumentParser) -> argparse.ArgumentParser.parse_args:
    """Validate arguments"""
    args = parser.parse_args()

    if args.pixel and args.average:
        print("Both --pixel and --average is used, this will result in only the average image to be created (overwrite image)")

    if args.pixel or args.average:
        if not args.input_path or not args.output_path:
            parser.error("Need --input-path and --output-path when using --pixel or --average")

    if args.pixel:
        if not args.size and not args.pixel_count:
            parser.error("Need --size or --pixel-count when using --pixel")
        elif args.size and args.pixel_count:
            parser.error("Using both --size and --pixel-count is conflicting")

    if args.create:
        if not args.output_path or not args.size or not args.color:
            parser.error("Need --output-path, --size and --color when using --create")

    if args.resize:
        if not args.size or not args.output_path or not args.input_path:
            parser.error("Need --output-path, --input-path and --size when using --resize")

    if args.pixel_count and not args.pixel:
        parser.error("Are you missing --pixel?")

    return args
