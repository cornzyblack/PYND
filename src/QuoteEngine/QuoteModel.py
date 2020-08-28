"""
This module contains a Quote Model which models a quote that consists of
a body text and an Author

Examples:
	>>> from QuoteEngine import QuoteModel
	>>> quote = QuoteModel("This is a good docstring", "Theo")
	>>> print(quote)
	>>> "This is a good docstring" - Theo
"""

class QuoteModel(object):
	"""
	This is a class for Quotes containing Body and Author

	Args:
		body (str): The body text of a quote
		author (str): The author of a quote

	Attributes:
		body (str): This is where the body text of a quote is stored
		author (str): This is where the author of a quote is stored
	"""
	def __init__(self, body:str, author:str):
		self.body = body
		self.author = author

	def __str__(self):
		result = "\"{}\" - {}".format(self.body, self.author)
		return result
