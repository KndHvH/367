'''
Escreva um programa para aprovar o empréstimo bancário para compra
 de uma casa. O programa deve perguntar o valor da casa a comprar,
 o salário e a quantidade de anos a pagar. O valor da prestação
 mensal não pode ser superior a 30% do salário. Calcule o valor da
 prestação como sendo o valor da casa a comprar dividido pelo
 número de meses a pagar.
'''
valor_casa=float(input("Digite o valor da casa: "))
salario=float(input("Digite o salario: "))
anos=int(input("Digite quantos anos de pagamento: "))

pmensal=valor_casa/anos

resposta=("Emprestimo Aprovado!")

if(pmensal>(salario*0.3)):
    resposta = ("Emprestimo Recusado!")

print(resposta)



