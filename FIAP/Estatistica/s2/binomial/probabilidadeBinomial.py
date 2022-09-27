
def main():
    # intervalo da probabilidade
    Xs = [0, 1, 2]

    # n total
    n = 20

    # sucesso
    p = 0.02

    q = 1-p

    total = 0

    for x in Xs:
        result = proba(x, n, p, q)
        print(f'X={x}: {result}')
        total += result

    print(f'P{Xs}=', total)
    print(f'1 - P{Xs} =', 1 - total)


def proba(x: int, n: int, p: float, q: float) -> float:
    """calcula a probabilidade de X

    Args:
        x (int): x
        n (int): n total
        p (int): p sucesso
        q (int): p fracasso

    Returns:
        float: probabilidade
    """

    result = combinacao(x, n) * p**x * q**(n-x)

    return result


def combinacao(x: int, n: int) -> float:
    """combinacao de x e n

    Args:
        x (int): x
        n (int): n

    Returns:
        float: resultado
    """
    result = fatorial(n) / (fatorial(x)*fatorial(n-x))
    return result


def fatorial(x: int) -> float:
    """calcula fatorial

    Args:
        x (int): numero

    Returns:
        float: resultado do fatorial
    """
    total = 1
    while x > 0:
        total *= x
        x -= 1
    return total


if __name__ == '__main__':
    main()
