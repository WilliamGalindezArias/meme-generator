from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import pandas as pd


class CSVIngestor(IngestorInterface):
    """ Checks if the file provided is CSV by using parse classmethod and extratcs quote from CSV

    Input: path
    Output: QuoteModel object
    """
    extension = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Error ingesting. File extension not supported')

        try:
            csv = pd.read_csv(path, header=0)

            return [QuoteModel(data_row['body'], data_row['author']) for index, data_row in csv.iterrows()]

        except:
            print("Error parsing CSV file")


