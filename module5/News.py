from typing import List

from module5.Publication import Publication


class News(Publication):

    def __init__(self, text: List[str], city: str):
        super().__init__(text)
        self.city = city

    def header(self) -> str:
        return "HOT NEWS !!!".ljust(50, "-")

    def footer(self) -> str:
        formatted_date_time = self.pub_datetime.strftime(self.DATE_TIME_FORMAT)
        return f"{self.city}, {formatted_date_time}".rjust(50, "-")
