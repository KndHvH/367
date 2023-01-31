

def main():
    # intervalo da probabilidade
    Xs = [2,3,4,5]

    # lambda
    lam = 2.5 

    
    # euler
    e = 2.718281828459045

    total = 0

    for x in Xs:
        result = proba(x, lam, e)
        print(f'X={x}: {result}')
        total += result

    print(f'P{Xs}=', total)
    print(f'1 - P{Xs} =', 1 - total)


def proba(x: int, lam, e) -> float:
    """calcula a probabilidade de X

    Args:

    Returns:
        float: probabilidade
    """

    result = (e**-lam * lam**x)/fatorial(x)

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
