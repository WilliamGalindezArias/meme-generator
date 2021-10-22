"""" Abstract Class used to verify that file types are compatibles with the Ingestor """

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """ Abstract Class to interface with the ingestor"""

    extension = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """ Takes a file path then:
         1. Extracts the extension
         2. Checks if the extension extracted is in the extension list
         3. returns a boolean depending of step 2 """
        f_ext = path.split('.')[-1]
        return f_ext in cls.extension


    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
