from dataclasses import dataclass
from typing import Tuple
from PIL import Image 


@dataclass
class RgbColor:
    red : int = 0
    green : int = 0
    blue : int = 0
    average : Tuple[int, int, int] = None

    def add_rgb(self, rgb_values: Tuple[int, int, int]):
        self.red += rgb_values[0]
        self.green += rgb_values[1]
        self.blue += rgb_values[2]

    def calculate_average(self, total_pixels: int):
        self.average = (self.red // total_pixels, self.green // total_pixels, self.blue // total_pixels)

    def __str__(self) -> str:
        return f"{self.red}, {self.green}, {self.blue}"


@dataclass
class Size:
    width: int
    height: int

    def __str__(self) -> str:
        return f"{self.width}, {self.height}"


def load_image(image_path: str):
    image = Image.open(image_path)
    px = image.load()
    return image, px
