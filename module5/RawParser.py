import os.path
import pathlib
from typing import List, Dict

from module4 import string_object_ref as sof
from module5.InputException import InputException


class RawParser:
    DEFAULT_FILE_PATH = os.path.join(pathlib.Path().resolve(), 'landing', 'raw-publications.txt')

    def __init__(self, file_path):
        self.file_path = file_path

    def parse_raw_file(self):
        return self.__get_pub_objects(self.__read_file())

    def __read_file(self) -> List[str]:
        with open(self.file_path) as file:
            lines = file.readlines()
        return lines

    def __get_pub_objects(self, lines: List[str]) -> List[Dict[str, str]]:
        try:
            publications = []
            for line in lines:
                objs = line.split(";")
                pub = {'type': objs[0].lower().replace(" ", ""),
                       'text': self.__normalize_pub_text(objs[1]),
                       'spec_info': objs[2].capitalize()}
                publications.append(pub)
            return publications
        except Exception:
            raise InputException("Wrong file format. Please read documentation.")

    @staticmethod
    def __normalize_pub_text(raw_text: str) -> List[str]:
        text = sof.cleanup_raw_text(raw_text)
        raw_sentences = sof.split_text_by_sentences(text)
        return sof.capitalize_sentences(raw_sentences)

    def delete_raw_file(self):
        os.remove(self.file_path)
