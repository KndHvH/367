#3

salario=float(input("Digite o seu salario: "))

salario_novo=salario*1.15
if salario>1250:
    salario_novo=salario*1.1

print(salario_novo)






def permitidoBEber(idade):
    if(idade < 18):
        return False


