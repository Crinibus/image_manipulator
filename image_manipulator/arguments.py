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
        required=True,
    )

    parser.add_argument(
        "-out",
        "--output_path",
        help="path to output image",
        type=str,
        dest="output_path",
        metavar="path",
        required=True,
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
        action="store_true"
    )

    return validate_arguments(parser)


def validate_arguments(parser: argparse.ArgumentParser) -> argparse.ArgumentParser.parse_args:
    """Validate arguments"""
    args = parser.parse_args()

    if args.pixel_size and args.average:
        parser.error("Both --pixel and --average is used, this will result in only one image to be created")

    return args
