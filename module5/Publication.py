from abc import ABC, abstractmethod
from datetime import datetime


class Publication(ABC):
    DATE_FORMAT = "%d/%m/%Y"
    DATE_TIME_FORMAT = "%d/%m/%Y %H:%M"
    PUBLICATION_TYPES = ["News", "Private Ad", "Arabic Text"]

    def __init__(self, pub_text: [str]):
        self.pub_text = pub_text
        self.pub_datetime = datetime.now()

    @abstractmethod
    def header(self) -> str:
        pass

    def body(self) -> str:
        return "\n".join(self.pub_text)

    @abstractmethod
    def footer(self) -> str:
        pass
