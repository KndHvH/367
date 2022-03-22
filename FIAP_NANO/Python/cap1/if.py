nome=input("Digite seu nome: \n")
idade=int(input("Digite sua idade: \n"))
hiv=input("Paciente tem HIV?: ").upper()

if idade>=65:
    print("\n\n" + nome + " recebe atendimento preferencial!")
elif hiv=='SIM':
    print("\n\n"+ nome + " deve ser direcionado a ala especial!" )
else:
    print("\n\n" + nome + " recebe atendimento regular!")

