
salario_bruto = float(input("Digite seu salário bruto: (R$) "))
dependentes = int(input("Digite o numero de dependentes: "))
outros_descontos = float(input("Digite possiveis outros descontos no salario: (R$) "))

inss=0
aliquota_inss = 7.5
if salario_bruto > 1212:
    aliquota_inss = 9
if salario_bruto > 2427.35:
    aliquota_inss = 12
if salario_bruto > 3641.03:
    aliquota_inss = 14
if salario_bruto > 7087.22:
    inss = 828.39

if inss == 0:
    inss = salario_bruto * (aliquota/100)


base_calculo = salario_bruto - inss - (dependentes * 189.59)

aliquota_irrf = 0
deducao_irrf = 0

if base_calculo > 1903.98:
    aliquota_irrf = 7.5
    deducao_irrf = 142.8

if base_calculo > 2826.65:
    aliquota_irrf = 15
    deducao_irrf = 354.8

if base_calculo >  3751.05:
    aliquota_irrf = 22.5
    deducao_irrf = 636.13

if base_calculo >  4664.68:
    aliquota_irrf = 27.5
    deducao_irrf = 869.36

irrf = (base_calculo * (aliquota_irrf/100) - deducao_irrf)

salario_liquido = salario_bruto - inss - irrf - outros_descontos


print(f"Salario Bruto = R$ {salario_bruto:.2f}")
print(f"INSS = R$ {inss:.2f}")
print(f"IRRF = R$ {irrf:.2f}")
print(f"Outros Descontos = R$ {outros_descontos:.2f}")
print(f"Salario Liquido = {salario_liquido:.2f}")
