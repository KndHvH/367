

class Data:

    def __init__(self, day, month, year) -> None:

        self.day = day
        self.month = month
        self.year = year

    def format(self):
        print(f'{self.day}/{self.month}/{self.year}')