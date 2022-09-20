
def main():

    Xs = [0, 1, 2, 3]

    n = 10

    p = 0.05

    q = 0.95

    total = 0

    for x in Xs:
        result = proba(x, n, p, q)
        print(f'X={x}: {result}')
        total += result

    print(1-total)


def proba(x, n, p, q):

    result = combinasao(x, n) * p**x * q**(n-x)

    return result


def combinasao(x, n):
    result = fatorial(n) / (fatorial(x)*fatorial(n-x))
    return result


def fatorial(x):
    total = 1
    while x > 0:
        total *= x
        x -= 1
    return total


if __name__ == '__main__':
    main()
