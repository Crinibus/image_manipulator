import argparse
import pathlib


def argparse_setup() -> argparse.ArgumentParser.parse_args:
    """Setup and return argparse."""
    parser = argparse.ArgumentParser(description="Image Manipulator")

    parser.add_argument(
        "-in",
        "--input_path",
        help="path to input image to manipulate",
        type=pathlib.Path,
        # type=str,
        dest="input_path",
        metavar="path",
        # required=True,
    )

    parser.add_argument(
        "-out",
        "--output_path",
        help="path to output image",
        type=str,
        dest="output_path",
        metavar="path",
        # required=True,
    )

    parser.add_argument(
        "--pixel",
        help="create new image with pixels of size 'width', 'height' that are color averages in that area",
        type=int,
        nargs=2,
        dest="pixel_size",
        metavar=("width", "height"),
    )

    parser.add_argument(
        "-a",
        "--average",
        help="create new image that that the average color of input image",
        action="store_true",
    )

    parser.add_argument(
        "--create",
        help="create a image of a specified size --size and color with flag --color",
        action="store_true",
    )

    parser.add_argument(
        "--resize",
        help="resize an image to specified size --size",
        action="store_true",
    )

    parser.add_argument(
        "--size",
        help="specify size",
        type=int,
        nargs=2,
        dest="size",
        metavar=("width", "height"),
    )

    parser.add_argument(
        "--color",
        help="specify color",
        type=str,
    )

    return validate_arguments(parser)


def validate_arguments(parser: argparse.ArgumentParser) -> argparse.ArgumentParser.parse_args:
    """Validate arguments"""
    args = parser.parse_args()

    if args.pixel_size or args.average:
        if not args.input_path or not args.output_path:
            parser.error("Need --input_path and --output_path when using --pixel or --average")

    if args.create:
        if not args.output_path:
            parser.error("Need --output_path when using --create")

    if args.resize:
        if not args.size or not args.output_path or not args.input_path:
            parser.error("Need --output_path, --input_path and --size when using --resize")

    if args.pixel_size and args.average:
        parser.error("Both --pixel and --average is used, this will result in only one image to be created")

    return args
