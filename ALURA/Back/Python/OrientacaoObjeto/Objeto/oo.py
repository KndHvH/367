
class Conta:

    bank_code = '001'

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

    def __canWithdraw(self, value):
        limit = self.__money + self.__limit
        if value > limit:
            decision = input(
                f'Apenas pode sacar R${limit:.2f}, digite \'y\' para proseguir: ')

            if decision == 'y':
                return limit
            else:
                return 0
        return value

    def withdraw(self, value):

        value = self.__canWithdraw(value)

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

    @staticmethod
    def bank_codes():
        print('codes copied')
        return {'BB': '001',  'Caixa': '104', 'Bradesco': '237'}
