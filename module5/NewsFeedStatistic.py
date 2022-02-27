import csv
import re
from typing import Dict


class NewsFeedStatistic:

    def __init__(self, newsfeed_file_name):
        self.newsfeed_file_name = newsfeed_file_name
        self.text = self.__read_newsfeed()
        self.letters = self.__get_letters()

    def write_word_statistic(self, csv_file_name) -> None:
        with open(csv_file_name, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter='-')
            for word, count in self.__get_world_statistic().items():
                writer.writerow([word, count])

    def write_letter_statistic(self, csv_file_name) -> None:
        with open(csv_file_name, 'w') as csvfile:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(csvfile, fieldnames=headers, quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            for letter in set(self.letters.lower()):
                writer.writerow({'letter': letter,
                                 'count_all': self.__count_total_of_letter(letter),
                                 'count_uppercase': self.__count_upper_of_letter(letter),
                                 'percentage': self.__get_letter_percentage(letter)})

    def __read_newsfeed(self) -> str:
        with open(self.newsfeed_file_name, 'r') as newsfeed:
            return newsfeed.read()

    def __get_world_statistic(self) -> Dict[str, int]:
        frequency = {}
        text = self.__read_newsfeed()
        split_text = re.findall(r'\w+', text)
        for s in split_text:
            if s.isalpha() and len(s) >= 2:
                word = s.lower()
                count = frequency.get(word, 0)
                frequency[word] = count + 1
        return frequency

    def __get_letters(self) -> str:
        return ''.join([symbol for symbol in self.text if symbol.isalpha()])

    def __count_total_of_letter(self, letter: str) -> int:
        return self.letters.lower().count(letter)

    def __count_upper_of_letter(self, letter: str) -> int:
        return self.letters.count(letter.upper())

    def __get_letter_percentage(self, letter: str) -> float:
        return self.__count_total_of_letter(letter) / len(self.text) * 100
