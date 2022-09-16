
def dinamicAdd(*args):
    total = 0
    for i in args:
        total += i
    return total

print(dinamicAdd(1,2,3,4))