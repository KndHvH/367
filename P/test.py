class Biggest:
    def __init__(self, number=1, total=0) -> None:
        self.__number = number
        self.__total = total

    def showall(self):
        i = self.__number
        for j in (2, i):
            if i % j == 0:
                print(f'{i} divide por {j} resultando em {i/j}')

    @property
    def number(self):
        return self.__number

    @property
    def total(self):
        return self.__total

    @number.setter
    def number(self, number):
        self.__number = number

    @total.setter
    def total(self, total):
        self.__total = total


big = Biggest()

for i in range(1, 4000):
    print(i)
    total = 0

    for j in range(2, i):

        if i % j == 0:
            #print(f'{i} divide por {j} resultando em {i/j}')
            total += 1

        if total > big.total:
            big.total = total
            big.number = i

big.showall()
