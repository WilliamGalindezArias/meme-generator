"""" Realizes IngestorInterface  """
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel

from .DocsIngestor import DocxIngestor
from .CVSIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .txtIngestor import TxtIngestor


class Ingestor(IngestorInterface):
    """Realizes ingestor interfaces and encapsulate all helper classes"""

    ingestors = [TxtIngestor, DocxIngestor, PDFIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            print('path passed to can ingest', path)
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
