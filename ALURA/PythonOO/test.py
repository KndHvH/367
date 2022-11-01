

def make_account(id: int, name: str, value: float, limit: float) -> dict:
    account = {
        'numero': id,
        'titular': name,
        'saldo': value,
        'limite': limit
    }
    return account


def deposit(account: dict, value: float) -> dict:
    account['saldo'] += value

    return account


def withdraw(account: dict, value: float) -> dict:
    account['saldo'] -= value

    return account


def status(account: dict):
    print('Saldo:', account['saldo'])
