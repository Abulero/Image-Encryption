import os
import easygui
import random
from PIL import Image, ImageChops


def Decrypt(image, key):
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
    # Get image and key
    print('Please select the encrypted image')
    image_path = easygui.fileopenbox(os.getcwd())
    image = Image.open(image_path)

    print('Now select the corresponding encryption key')
    key_path = easygui.fileopenbox(os.getcwd())
    key = Image.open(key_path)

    # Decrypt image
    print('Decrypting...')
    decrypted_image = Decrypt(image, key)

    # saving
    decrypted_image.save('decrypted_image.png')
    print('Done')
