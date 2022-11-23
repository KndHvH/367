nome=input("Digite seu nome: ")
trabalho=input("Digite onde trabalha: ")
num_filhos=int(input("Digite o numero de filhos: "))
valor_banco=float(input("Digite valor do seu dinheiro no banco: "))

print("\n\n\n" + nome + " trabalha na empresa " + trabalho)
print(nome + " tem " + str(num_filhos) + " filhos ")
print(nome + " tem " + str(valor_banco) + "R$ no banco \n\n\n")

print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(trabalho))
print("O tipo de dado da variavel [qtde_filhos] é: ",type(num_filhos))
print("O tipo de dado da variavel [valor_banco] é: ",type(valor_banco))


