import enum
from abc import ABC, abstractmethod
from datetime import datetime


class Publication(ABC):
    DATE_FORMAT = "%d/%m/%Y"
    DATE_TIME_FORMAT = "%d/%m/%Y %H:%M"

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


class PublicationType(enum.Enum):
    news = 1
    privateAd = 2
    arabicText = 3
