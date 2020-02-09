from abc import ABC, abstractmethod
from pathlib import Path
from typing import List
from docx import Document
import pandas as pd
import subprocess
import os
from .QuoteModel import QuoteModel

"""
This module also contains Ingestor Classes  for 
parsing various File Formats, and an Ingestor class for dyanmically
parsing any of the supported files.

The file formats supported are: PDF, txt, DOCX and CSV

	>>> from QuoteIngestors import TextIngestor
	>>> quote_list = TextIngestor.parse("quotes.txt")
	>>> print(quote_list[0])
	>>> "This is a good docstring" - Theo

	>>> from QuoteIngestors import PdfIngestor
	>>> quote_list = PdfIngestor.parse("quotes.pdf")
	>>> print(quote_list[0])
	>>> "This is a good docstring" - Theo

	>>> from QuoteIngestors import DocxIngestor
	>>> quote_list = DocxIngestor.parse("quotes.docx")
	>>> print(quote_list[0])
	>>> "This is a good docstring" - Theo

	>>> from QuoteIngestors import CsvIngestor
	>>> quote_list = CsvIngestor.parse("quotes.csv")
	>>> print(quote_list[0])
	>>> "This is a a Csv Quote" - Theo

	>>> from QuoteIngestors import Ingestor
	>>> quote_list = Ingestor.parse("quotes.csv")
	>>> print(quote_list[0])
	>>> "This is a Csv docstring" - Theo

"""

class IngestorInterface(ABC):

	@classmethod
	def can_ingest(cls, path:str) -> bool:
		"""checks if the file in the path can be parsed"""
		return Path(path).suffix in ['.csv', '.txt', '.pdf', '.docx']
	
	@classmethod
	@abstractmethod
	def parse(cls, path:str) -> List[QuoteModel]:
		"""This method should implement the parse method"""
		pass

class TextIngestor(IngestorInterface):
	@classmethod
	def parse(cls, path:str):
		"""This method parses a txt file"""
		quote_models = []
		with open(path, "rb") as file:
			f = file.readlines()
		for line in f:
			if "-" in line.decode():
				quote_models = [QuoteModel(*line.decode().rstrip().split("-"))]
		
		return quote_models
		

class DocxIngestor(IngestorInterface):
	@classmethod
	def parse(cls, path:str):
		"""This method parses a DOCX file"""
		quote_models = []
		document = Document(path)
		paragraphs = document.paragraphs
		clean_paragraphs = list(filter(lambda p: "-" in p.text.strip(), paragraphs))
		list_of_paragraphs = [p.text.strip() for p in clean_paragraphs]
		quote_models = [QuoteModel(*(p.split("-"))) for p in list_of_paragraphs]
		return quote_models
	

class PdfIngestor(IngestorInterface):
	@classmethod
	def parse(cls, path:str):
		"""This method parses a PDF file"""
		quote_models = []
		folder_path_name = Path(os.path.dirname(path))
		file_name = os.path.basename(os.path.splitext(path)[0])
		
		save_file_path = os.path.join(folder_path_name, "tmp_pdf_output.txt")
		subprocess.run(f"pdftotext -raw {path} {save_file_path}")
		quote_models = TextIngestor.parse(save_file_path)
		os.remove(save_file_path)
		return quote_models



class CsvIngestor(IngestorInterface):
	@classmethod
	def parse(cls, path:str):
		"""This method parses a CSV file"""
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

class Ingestor(IngestorInterface):
	
	@classmethod
	def parse(cls, path:str):
		"""This method dynamically parses a CSV, PDF, DOCX or txt file"""
		quote_models = None
		if IngestorInterface.can_ingest(path):
			ingestor_dict =  {'csv':CsvIngestor, 'txt':TextIngestor,
				'pdf':PdfIngestor, 'docx': DocxIngestor}
			file_suffix = Path(path.lower()).suffix
			quote_models = ingestor_dict[file_suffix[1:]].parse(path)
		else:
			pass
		return quote_models

	
