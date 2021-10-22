from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import subprocess
import os


class PDFIngestor(IngestorInterface):
    """Ingests PDF files by running a subprocess """
    extension = ['pdf']
    temporary_txt_path = "temp.txt"
    pdf_cli = 'pdftotext'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Error ingesting. File extension not supported')
        quotes = []
        try:
            subprocess.run([cls.pdf_cli, path, cls.temporary_txt_path])
            with open(cls.temporary_txt_path, mode='r') as file:
                for line in file:
                    line = line.strip('\n\r').strip()
                    if len(line) > 0:
                        text_line = line.split('-')
                        quote = QuoteModel(text_line[0], text_line[1])
                        quotes.append(quote)
                os.remove(cls.temporary_txt_path)

                return quotes


        except:
            print("Error trying to parse PDF file")
