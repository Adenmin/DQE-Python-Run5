from datetime import datetime
from typing import List

from module5.ArabicText import ArabicText
from module5.InputException import InputException
from module5.News import News
from module5.PrivateAd import PrivateAd
from module5.Publication import Publication, PublicationType, PublicationMethod
from module5.RawParser import RawParser


class Publisher:

    @staticmethod
    def get_pub_method() -> PublicationMethod:
        pub_method = int(input("How you can want to send a publication\n"
                               "1 - manual\n2 - from file\n"
                               "Please enter number for one of the publication type: "))
        return PublicationMethod(pub_method)

    @staticmethod
    def get_publication_type() -> PublicationType:
        pub_type = int(input("Welcome to Publisher!\n"
                             "1 - News\n2 - Private Ad\n3 - Arabic Text\n"
                             "Please enter number for one of the publication type: "))
        if pub_type not in [pt.value for pt in PublicationType]:
            raise InputException("Publication type is not supported.")
        return PublicationType(pub_type)

    @staticmethod
    def get_publication_text() -> List[str]:
        row_count = int(input("Count of text row: "))
        if row_count <= 0:
            raise InputException("Row count should be more than 0.")
        pub_text = []
        for row in range(0, row_count):
            try:
                line = input(f"Type row {row + 1}: ")
            except EOFError:
                break
            pub_text.append(line)
        return pub_text

    @staticmethod
    def get_specific_info(pub_type: PublicationType) -> str:
        if pub_type is PublicationType.news:
            return input("Enter City of news: ")
        elif pub_type is PublicationType.privateAd:
            exp_date = input("Enter expiration date in format like 01/01/2023 : ")
            if exp_date == datetime.strptime(exp_date, Publication.DATE_FORMAT):
                raise InputException("Date format is not supported.")
            if datetime.strptime(exp_date, Publication.DATE_FORMAT) < datetime.now():
                raise InputException("We don't publish expired ads.")
            return exp_date
        else:
            return ""

    @staticmethod
    def build_publication(pub_type: PublicationType, pub_text: List[str], spec_info: str) -> Publication:
        if pub_type is PublicationType.news:
            return News(pub_text, spec_info)
        elif pub_type is PublicationType.privateAd:
            return PrivateAd(pub_text, spec_info)
        elif pub_type is PublicationType.arabicText:
            return ArabicText(pub_text)

    @staticmethod
    def write_to_newsfeed(pub: Publication) -> None:
        with open("newsfeed.txt", "a") as newsfeed:
            newsfeed.write(f"{pub.header()}\n{pub.body()}\n{pub.footer()}\n\n\n")

    @staticmethod
    def get_file_path() -> str:
        if int(input("1 - use default landing folder and file\n"
                     "2 - use custom path to your file\n"
                     "Choose file location variant: ")) == 1:
            return RawParser.DEFAULT_FILE_PATH
        else:
            return input("Type full path to your file with publications: ")
