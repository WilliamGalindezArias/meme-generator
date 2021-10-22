from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TxtIngestor(IngestorInterface):
    """ Checks if the file provided is .txt by using parse classmethod and extracts quote from txt

    Input: path
    Output: QuoteModel object
    """
    extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Error ingesting!. File extension not supported')

        try:
            quotes = []
            with open(path, mode='r') as file:
                text_lines = file.readlines()
                for text_line in text_lines:
                    text_line = text_line.strip('\n').split('-')
                    if len(text_line) > 1:
                        new_quote = QuoteModel(text_line[0], text_line[1])
                        quotes.append(new_quote)

            return quotes

        except:
            print("Error parsing txt file")

