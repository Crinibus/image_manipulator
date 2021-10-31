from PIL import Image
from math import floor


def main():
    input_image_name = input("Enter name of image in folder \"input\"\n>")
    image = Image.open(f'input/{input_image_name}')
    pixels = image.load()
    print("Size of input image:", image.size)

    desired_image_size = input("Enter desired size of image \"w,h\"\n>")
    desired_width = int(desired_image_size.split(',')[0])
    desired_height = int(desired_image_size.split(',')[1])
    # image_name = input("Enter name for output image\n>")
 
    desired_image = Image.new('RGB', (desired_width, desired_height), "white")
    desired_image_pixels = desired_image.load()

    pixel_width = floor(image.size[0] / desired_width)
    pixel_height = floor(image.size[1] / desired_height)

    for x in range(desired_width):
        for y in range(desired_height):
            # sum color
            sum_red_color = 0
            sum_green_color = 0
            sum_blue_color = 0

            for xPixel in range(pixel_width):
                for yPixel in range(pixel_height):
                    pixel = pixels[xPixel + x * pixel_width, yPixel + y * pixel_height]
                    sum_red_color += pixel[0]
                    sum_green_color += pixel[1]
                    sum_blue_color += pixel[2]
            
            average_red = int(sum_red_color / (pixel_width * pixel_height))
            average_green = int(sum_green_color / (pixel_width * pixel_height))
            average_blue = int(sum_blue_color / (pixel_width * pixel_height))

            desired_image_pixels[x, y] = (average_red, average_green, average_blue)
    
    desired_image.save("output/resize.png")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\Keyboard cancelled")
