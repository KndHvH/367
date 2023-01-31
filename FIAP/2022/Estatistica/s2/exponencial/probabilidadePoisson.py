

def main():
    # probabilidade
    x = 100

    # parametro
    paramA = 1/80
    paramB = 1/100

    # euler
    e = 2.718281828459045


    resultA = proba(x, paramA, e)
    resultB = proba(x, paramB, e)



    print(f'P{x}=', resultA)
    print(f'1 - P{x} =', 1 - resultA)

    print(f'P{x}=', resultB)
    print(f'1 - P{x} =', 1 - resultB)


def proba(x, param, e) -> float:

    result = (e**(-param*0))- (e**(-param*x))

    return result


def fatorial(x: int) -> float:
    total = 1
    while x > 0:
        total *= x
        x -= 1
    return total


if __name__ == '__main__':
    main()
