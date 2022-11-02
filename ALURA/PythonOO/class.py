
class Conta:

    def __init__(self, id: int, name: str, value, limit=1000.0) -> None:

        print('Contruindo', self)

        self.__id = id
        self.__titular = name
        self.__saldo = value
        self.__limite = limit

    def extract(self):
        print(f'Conta: {self.__id}')
        print(f'Nome: {self.__titular}')
        print(f'Saldo: R${self.__saldo:.2f}')
        print(f'Limite: R${self.__limite:.2f}')

    def deposit(self, value):

        self.__saldo += value

    def withdraw(self, value):

        self.__saldo -= value
