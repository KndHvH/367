import datetime

class WeirdClock:
    def __init__(self) -> None:
        self.__time = datetime.datetime.now()

    def update(self) -> bool:
        if self.__time != datetime.datetime.now():
            self.__time = datetime.datetime.now()
            return True
        return False

    def __str__(self) -> str:
        now = self.get_time_format()
        now_int = [int(i) for i in now]
        return f'\nDia: {now_int[0]/now_int[1]:.2f}\nHora: {now_int[2]/now_int[3]:.2f}'
    
    def get_time_format(self) -> list:
        return self.__time.strftime('%d/%m/%H/%M').split('/')


def main():
    now = WeirdClock()
    print(now)

    while True:
        if now.update():
            print(now)


if __name__ == '__main__':
   main()
