import os
import easygui
import random
from PIL import Image


if __name__ == '__main__':
    # Get image
    image_path = easygui.fileopenbox(os.getcwd())

    # Generate key from image
    image = Image.open(image_path)
    
    key = Image.new('RGB', image.size)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            r = random.nextint(256)
            g = random.nextint(256)
            b = random.nextint(256)

            key.pupixel((x, y), (r, g, b))

    # Encrypt image and save it
    encrypted_image = image^key

    # Showing results
    image.show()
    key.show()
    encrypted_image.show()
    (encrypted_image^key).show()
