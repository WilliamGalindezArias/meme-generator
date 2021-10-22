from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
from docx import Document


class DocxIngestor(IngestorInterface):
    """ Checks if the file provided is .docx by using parse classmethod and extracts quote from docx

        Input: path
        Output: QuoteModel object
        """
    extension = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Error ingesting. File extension not supported')
        quotes = []
        try:

            doc = Document(path)

            for paragraph in doc.paragraphs:
                if paragraph.text != "":
                    text_line = paragraph.text.split('-')
                    quote = QuoteModel(text_line[0], text_line[1])
                    quotes.append(quote)

            return quotes

        except:
            print("Error parsing docx file")