
class Conta:

    def __init__(self, id: int, name: str, value: float, limit: float = 1000.0) -> None:

        print('Contruindo', self)

        self.numero = id
        self.titular = name
        self.saldo = value
        self.limite = limit
