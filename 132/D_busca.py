"""
Todos os equipamentos "impressora" receberão uma depreciação (desvalorização após certo
período) de 10%. Monte o código que seria responsável por alterar o valor de todos os
equipamentos "impressora".
"""

equip=[]
valor=[]
x='s'

while x=='s':
    equip.append(input("Digite o tipo de equipamento: ").upper())
    valor.append(input("Digite o valor do equipamento: ").upper())

    x=input("Digite \'S\' para cadastrar outro produto: ").upper()

for i in range(0,len(equip)):
    if equip[i] == "IMPRESSORA":
        valor[i] = valor[i]*0.9
