import json
import os.path
import pathlib
import xml.etree.ElementTree as ET
from typing import List, Dict

from module4 import string_object_ref as sof
from module5.InputException import InputException


class RawParser:
    DEFAULT_LANDING_DIR = os.path.join(pathlib.Path().resolve(), 'landing')

    def __init__(self, file_path):
        self.file_path = file_path

    def parse_raw_file(self):
        return self.__read_file()

    def __read_file(self) -> List[Dict[str, str]]:
        if pathlib.Path(self.file_path).suffix == '.txt':
            return self.__normalize_raw_pubs(self.__get_raw_pubs_from_txt())
        if pathlib.Path(self.file_path).suffix == '.json':
            return self.__normalize_raw_pubs(self.__get_raw_pubs_from_json())
        if pathlib.Path(self.file_path).suffix == '.xml':
            return self.__normalize_raw_pubs(self.__get_raw_pubs_from_xml())
        else:
            file_format = pathlib.Path(self.file_path).suffix
            raise InputException(f"{file_format} file isn't supported.")

    def __get_raw_pubs_from_xml(self):
        try:
            xml_root = ET.parse(self.file_path).getroot()
            publication = []
            for p in xml_root.iter('pub'):
                pub = {'type': p.get('type'),
                       'text': p.find('text').text,
                       'spec_info': p.find('text').get('spec_info')}
                publication.append(pub)
            return publication
        except Exception:
            raise InputException('Incorrect XML schema.')

    def __get_raw_pubs_from_json(self) -> List[Dict[str, str]]:
        try:
            return json.load(open(self.file_path))['pubs']
        except Exception:
            raise InputException('Incorrect JSON schema.')

    def __get_raw_pubs_from_txt(self) -> List[Dict[str, str]]:
        try:
            with open(self.file_path) as file:
                lines = file.readlines()
            publications = []
            for line in lines:
                objs = line.split(";")
                pub = {'type': objs[0],
                       'text': objs[1],
                       'spec_info': objs[2]}
                publications.append(pub)
            return publications
        except Exception:
            raise InputException('Incorrect text file.')

    def __normalize_raw_pubs(self, raw_pubs: List[Dict[str, str]]) -> List[Dict[str, str]]:
        for pub in raw_pubs:
            pub['type'] = pub['type'].lower().replace(" ", "")
            pub['text'] = self.__normalize_pub_text(pub['text'])
            if pub['spec_info'] is not None:
                pub['spec_info'] = pub['spec_info'].capitalize()
        return raw_pubs

    @staticmethod
    def __normalize_pub_text(raw_text: str) -> List[str]:
        text = sof.cleanup_raw_text(raw_text)
        raw_sentences = sof.split_text_by_sentences(text)
        return sof.capitalize_sentences(raw_sentences)

    def delete_raw_file(self):
        os.remove(self.file_path)
