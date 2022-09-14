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


total = len(list)
promoters = 0
detractors = 0
neutral = 0

for i in list: 
    if i <= 6:
        detractors +=1
        print(f'{i} = detractor')
    elif i >= 9:  
        promoters += 1 
        print(f'{i} = promotor')
    else:
        neutral += 1
        print(f'{i} = neutral')



pcemPro = (promoters/total)*100
pcemNeu = (neutral/total)*100
pcemDet = (detractors/total)*100

nps = pcemPro - pcemDet

npsString = 'Excelente'
if nps < 75:
    npsString = 'Muito Bom'
if nps < 50:
    npsString = 'Razoavel'
if nps < 0:
    npsString = 'Ruim' 


print(f'Porcentagem Pro {pcemPro:.2f}%')    
print(f'Porcentagem Neutros {pcemNeu:.2f}%')
print(f'Porcentagem Det {pcemDet:.2f}%')
print(f'Nps Total Score: {nps:.2f}')
print(f'NPS {npsString}')

print('hello from ubuntu')