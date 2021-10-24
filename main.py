from image_manipulator import load_image, set_pixels_average
from image_manipulator import create_image_with_color, get_average_color


def main():
    #pixel_art()
    average_color()


def pixel_art():
    image, px = load_image("input/rainbow.png")
    set_pixels_average(px, image.size, (64, 64))
    image.save("output/rainbow_pixel.png")


def average_color():
    input_image, input_px = load_image("input/rainbow.png")
    average_color = get_average_color(input_px, input_image.size)
    image, px = create_image_with_color(average_color, (200,200))
    image.save("output/rainbow_average_color.png")


if __name__ == "__main__":
    main()
