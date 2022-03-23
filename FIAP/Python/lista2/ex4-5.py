'''
Faça um programa que leia 2 notas de um aluno,
calcule a média e imprima aprovado ou reprovado
(para ser aprovado a média deve ser no mínimo 6).
'''
n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))

media= (n1*0.4) + (n2*0.6)

resultado=f"Aprovado com média {media:.1f}"

if media<6:
    resultado = f"Exame com média {media:.1f}!!"

if media<4:
    resultado = f"Reprovado com média {media:.1f}!!"

print(resultado)