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
    print('Please select the image to be encrypted')
    image_path = easygui.fileopenbox(os.getcwd())
    image = Image.open(image_path)

    # Generate key from image
    print('Generating key...')
    key = Image.new('RGB', image.size)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            key.putpixel((x, y), (r, g, b))
    print('Done')

    # Encrypt image
    print('Encrypting...')
    encrypted_image = Encrypt(image, key)

    # Saving
    encrypted_image.save('encrypted_image.png')
    key.save('key.png')
    print('Done')