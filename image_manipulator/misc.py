from typing import Generator, Tuple
from dataclasses import dataclass
from PIL import Image
from PIL.PyAccess import PyAccess


@dataclass
class RgbColor:
    red: int = 0
    green: int = 0
    blue: int = 0
    average: Tuple[int, int, int] = None

    def add_rgb(self, rgb_values: Tuple[int, int, int]) -> None:
        self.red += rgb_values[0]
        self.green += rgb_values[1]
        self.blue += rgb_values[2]

    def calculate_average(self, total_pixels: int) -> Tuple[int, int, int]:
        self.average = (self.red // total_pixels, self.green // total_pixels, self.blue // total_pixels)

    @property
    def hex(self) -> str:
        rgb_values = [self.red, self.green, self.blue]
        hex_values = [format(rgb_value, "02x") for rgb_value in rgb_values]
        return f"#{''.join(hex_values)}"

    @property
    def average_hex(self) -> str:
        hex_values = [format(rgb_value, "02x") for rgb_value in self.average]
        return f"#{''.join(hex_values)}"

    @staticmethod
    def from_hex_to_rgb(hex_value: str) -> Tuple[int, int, int]:
        hex_value = hex_value.strip("#")
        # convert from base 16 to base 10 in pairs of two digits
        return tuple([int(hex_value[i : i + 2], 16) for i in range(0, len(hex_value), 2)])

    @staticmethod
    def is_hex(color_input: str) -> bool:
        if len(color_input) != 7 or not color_input.startswith("#"):
            return False

        try:
            return isinstance(int(color_input[1:7], 16), int)
        except ValueError:
            return False

    def __str__(self) -> str:
        return f"{self.red}, {self.green}, {self.blue}"


@dataclass
class Size:
    width: int
    height: int

    def __str__(self) -> str:
        return f"{self.width}, {self.height}"

    def __getitem__(self, pos) -> int:
        if pos == 0:
            return self.width
        elif pos == 1:
            return self.height

        raise ValueError("size index out of range")


def load_image(image_path: str, image_mode: str = "RGBA") -> Tuple[Image.Image, PyAccess]:
    """Load image. Default image mode is 'RGBA'.
    Return image and pixels of image"""
    image = Image.open(image_path).convert(image_mode)
    pixels = image.load()
    return image, pixels


def iterate_pixels(width, height) -> Generator[Tuple[int, int], None, None]:
    for x in range(0, width):
        for y in range(0, height):
            yield x, y


def iterate_image_pixels(image: Image.Image) -> Generator[Tuple[int, int], None, None]:
    image_width, image_height = image

    for pixel_xy in iterate_pixels(image_width, image_height):
        yield pixel_xy
