from abc import ABC, abstractmethod
from pathlib import Path
from typing import List
from docx import Document
import pandas as pd


class QuoteModel(object):
	def __init__(self, body:str, author:str):
		self.body = body
		self.author = author

	def __str__(self):
		result = "\"{}\" - {}".format(self.body, self.author)
		return result

class IngestorInterface(ABC):

	@classmethod
	def can_ingest(cls, path:str) -> bool:
		return Path(path).suffix in ['.csv', '.pdf', '.docx']
	
	@classmethod
	@abstractmethod
	def parse(cls, path:str) -> List[QuoteModel]:
		pass

class TextIngestor(IngestorInterface):
	def parse(cls, path:str):
		quote_models = []
		with open(path, "rb") as file:
			f = file.readlines()
		quote_models = [QuoteModel(*line.decode().rstrip().split("-")) for line in f]
		
		return quoteModels

class DocxIngestor(IngestorInterface):
	def parse(cls, path:str):
		document = Document(path)
		list_of_paragraphs = [paragraph.text.strip() for paragraph in document.paragraphs if "-" in paragraph.text.strip()]
		quote_models = [QuoteModel(*(paragraph.split("-"))) for paragraph in list_of_paragraphs]
		return quote_models
	

class PdfIngestor(IngestorInterface):
	def parse(cls, path:str):
		pass


class CsvIngestor(IngestorInterface):
	def parse(cls, path:str):
		quote_models = []
		try:
			df = pd.read_csv(path)
			for idx, row in df.iterrows():
				quote_models.append(QuoteModel(row['body'], row['author']))
		except pd.errors.ParserError:
			print("Invalid File")
		except OSError:
			print("Could not find the File")
		return quote_models