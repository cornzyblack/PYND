## QuoteEngine Module
	 
### Classes:

#### - QuoteModel

> This class models the contents of a Quote.

#### - PdfIngestor
> This class ingests the text content in a PDF containing Quotes.

#### - CsvIngestor
> This class ingests the text content in a PDF file containing Quotes.

#### - TxtIngestor
> This class ingests the text content in a txt file containing Quotes.

#### - DocxIngestor
> This class ingests the text content in a DOCX file containing Quotes.

 ### Dependencies:
- python-docx
- Pandas
- pdftotext

### Examples
    >>> from QuoteEngine import QuoteModel
    >>> quote = QuoteModel("This is a good docstring", "Theo")
    >>> print(quote)
    >>> "This is a good docstring" - Theo

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
