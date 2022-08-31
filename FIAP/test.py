from calendar import c
from re import X


list = [
        [
            'a', 'b', 'c'
        ],
        [
            'a', 'c', 'd'
        ],
        [
            'a'
        ],
]
total = {}

for i in list:
    for j in i:
        total.setdefault(j,0)

        total[j] += 1

print(total)


