import enum
from abc import ABC, abstractmethod
from datetime import datetime

from module5.InputException import InputException


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

    @staticmethod
    def from_str(raw_pub_type):
        if raw_pub_type == "news":
            return PublicationType.news
        if raw_pub_type == "privatead":
            return PublicationType.privateAd
        if raw_pub_type == "arabictext":
            return PublicationType.arabicText
        else:
            raise InputException("Publication type is not supported.")


class PublicationMethod(enum.Enum):
    manual = 1
    fromFile = 2
