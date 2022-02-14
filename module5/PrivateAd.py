from datetime import datetime

from module5.Publication import Publication


class PrivateAd(Publication):

    def __init__(self, text, exp_date):
        super().__init__(text)
        self.exp_date = exp_date

    def __days_left(self) -> int:
        delta = datetime.strptime(self.exp_date, self.DATE_FORMAT) - self.pub_datetime
        return delta.days

    def header(self) -> str:
        return "Private Ad".ljust(50, "-")

    def footer(self) -> str:
        return f"Actual until: {self.exp_date}, {self.__days_left()} days left".rjust(50, "-")
