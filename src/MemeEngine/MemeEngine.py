"""Loads, resizes and adds a caption to an image."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from random import randint
import os


FONT = "./fonts/impact.ttf"


class MemeEngine():
    """Generates memes"""

    def __init__(self, output_directory):
        self.output_directory = output_directory

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

    def make_meme(self, image_path, text, author, width=500) -> str:
        """Creates a meme with a quote and its author

        inputs:
            image_path: string - file location of the input image
            text: string - text on the meme image
            author: string - Quote author
            width: integer - width value, defaults to 500

        output:
        output_file_path: string - path to the output image


        """

        img = Image.open(image_path)
        ratio = (width / float(img.size[0]))
        height = ratio * float(img.size[1])
        resize_img = img.resize((width, height), resample=Image.NEAREST)
        draw_image = ImageDraw.Draw(resize_img)
        #font = ImageFont.load_default(size=20)
        font = ImageFont.truetype(FONT, 30)
        #font = ImageFont.truetype("arial.ttf", size=20)
        draw_image.text((40, 40), f'"{text}" \n- {author}', fill="white", font=font, align="center")
        output_file_path = Path(f'{self.output_directory}/{randint(0,100000000)}.jpg')

        try:
            resize_img.save(output_file_path)

        except FileNotFoundError:
            os.mkdir(output_file_path)
            resize_img.save(output_file_path)

        return output_file_path




