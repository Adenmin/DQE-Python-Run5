from typing import List

from module5.Publication import Publication


class ArabicText(Publication):

    def __init__(self, text: List[str]):
        super().__init__(text)

    def __translation_complexity(self) -> int:
        word_list = "\n".join(self.pub_text).split()
        return len(word_list)

    def header(self) -> str:
        return "نص عربي".ljust(50, ".")

    def body(self) -> str:
        arabic_text = []
        for row in self.pub_text:
            arabic_row = []
            words = row.split(" ")
            for word in words:
                arabic_row.append(word[::-1])
            arabic_row.reverse()
            arabic_text.append(" ".join(arabic_row))
        return "\n".join(arabic_text)

    def footer(self) -> str:
        return f"Translation complexity: {self.__translation_complexity()}".rjust(50, "-")
