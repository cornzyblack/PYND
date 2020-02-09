from PIL import Image, ImageDraw, ImageFont
from random import choice
import os
from pathlib import Path

"""
This module contains a MemeEngine Generator used to generate Memes

Examples:
	>>> from MemeGenerator import MemeEngine
	>>> meme_obj = MemeEngine("./pictures")
"""
class MemeEngine(object):
	"""
	This is a class for Generating custom Memes on Images.

	Args:
		folder_path (str): The folder path where the images should be saved 

	Attributes:
		save_folder_path (str): The folder path where the images should be saved 

	"""

	def __init__(self, folder_path):
		self.save_folder_path = folder_path

	def make_meme(self, img_path, text, author, width=500) -> str:
		"""Turn an Image into a Meme image"""
		if Path(img_path).suffix == '.png':
			pil_image = Image.open(img_path).convert("RGB")
		else:
			pil_image = Image.open(img_path)

		image_width, image_height = pil_image.size
		resize_width = image_width       
		resize_height = None
		text_position = choice([50, 100, 150, 200, 250, 300])
		font_file_name = "arial.ttf"
		
		fnt_text = ImageFont.truetype(font_file_name, size=25)
		fnt_author = ImageFont.truetype(font_file_name, size=20)
		text_shadow_color = "white"
		author_shadow_color = "black"
		
		aspect_ratio = image_width/image_height
		if image_width > width:
			resize_width  = width
			aspect_ratio = resize_width / image_height

		resize_height =  int(aspect_ratio *  image_height)

		pil_image = pil_image.resize((resize_width, resize_height))
		txt_obj = ImageDraw.Draw(pil_image)  

		txt_obj.text((10 - 1, text_position), text, font=fnt_text, fill=text_shadow_color)
		txt_obj.text((10 + 1, text_position), text, font=fnt_text, fill=text_shadow_color)
		txt_obj.text((10, text_position - 1), text, font=fnt_text, fill=text_shadow_color)
		txt_obj.text((10, text_position + 1), text, font=fnt_text, fill=text_shadow_color)
		
		txt_obj.text((10, text_position), text, font=fnt_text, fill="black")
			

		txt_obj.text((30 - 1, text_position + 35), author, font=fnt_author, fill=author_shadow_color)
		txt_obj.text((30 + 1, text_position + 35), author, font=fnt_author, fill=author_shadow_color)
		txt_obj.text((30, text_position + 35 - 1), author, font=fnt_author, fill=author_shadow_color)
		txt_obj.text((30, text_position + 35 + 1), author, font=fnt_author, fill=author_shadow_color)
		
		txt_obj.text((30, text_position + 35 ), author, font=fnt_author, fill="white")
		folder_path_name = Path(os.path.dirname(img_path))
		file_name = os.path.basename(os.path.splitext(img_path)[0])

		save_file_path = os.path.join(self.save_folder_path,
			file_name + "_meme"+ Path(img_path).suffix)

		pil_image.save(save_file_path)
		return save_file_path
