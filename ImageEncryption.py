import os
import easygui
import random
from PIL import Image, ImageChops


def Encrypt(image, key):
    encrypted_image = Image.new('RGB', image.size)

    width = image.size[0]
    height = image.size[1]

    for x in range(width):
        for y in range(height):
            image_pixel = image.getpixel((x, y))
            key_pixel = key.getpixel((x, y))

            new_pixel = (image_pixel[0]^key_pixel[0], image_pixel[1]^key_pixel[1], image_pixel[2]^key_pixel[2])

            encrypted_image.putpixel((x, y), new_pixel)

    return encrypted_image


if __name__ == '__main__':
    # Get image
    image_path = easygui.fileopenbox(os.getcwd())
    image = Image.open(image_path)

    # Generate key from image
    key = Image.new('RGB', image.size)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            key.putpixel((x, y), (r, g, b))

    # Encrypt image
    encrypted_image = Encrypt(image, key)

    # Showing results
    image.show()
    key.show()

    encrypted_image.show()

    # Unveiling the original image
    original_image = Encrypt(encrypted_image, key)

    original_image.show()
