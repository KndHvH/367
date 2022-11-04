
class Conta:

    def __init__(self, id: int, name: str, value=0.0, limit=1000.0) -> None:

        print('Contruindo', self)

        self.__id = id
        self.__name = name
        self.__money = value
        self.__limit = limit

    def extract(self):
        print(f'Conta: {self.__id}')
        print(f'Nome: {self.__name}')
        print(f'Saldo: R${self.__money:.2f}')
        print(f'Limite: R${self.__limit:.2f}')

    def deposit(self, value):

        self.__money += value

        self.extract()

    def withdraw(self, value):

        self.__money -= value

        self.extract()

    def transfer(self, value, destin):

        self.withdraw(value)

        destin.deposit(value)
    
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name.title()

    @property
    def money(self):
        return self.__money

    @property
    def limit(self):
        return self.__limit

    @name.setter
    def name(self, name):
        self.__name = name

    @limit.setter
    def limit(self, limit):
        self.__limit = limit