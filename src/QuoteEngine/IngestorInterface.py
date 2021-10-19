"""" Abstract Class used to verify that file types are compatibles with the Ingestor """

from abc import ABC
from typing import List
from QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """ Abstract Class to interface with the ingestor"""

    def __init__(self):
        pass

    @classmethod
    def can_ingest(cls, path) -> bool:
        """ Takes a file path and extracts the extension """
        f_ext = path.split('.')[-1]
        return f_ext


    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass


