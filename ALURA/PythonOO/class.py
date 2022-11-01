
class Conta:

    def __init__(self, id: int, name: str, value, limit=1000.0) -> None:

        print('Contruindo', self)

        self.id = id
        self.titular = name
        self.saldo = value
        self.limite = limit

    def extract(self):
        print(f'Conta: {self.id}')
        print(f'Nome: {self.titular}')
        print(f'Saldo: R${self.saldo:.2f}')

    def deposit(self, value):

        self.saldo += value

    def withdraw(self, value):

        self.saldo -= value
