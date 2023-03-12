# A energia média da radiação emitida por um corpo negro pode ser calculada usando a Lei de Planck
# , que relaciona a energia da radiação com a temperatura e a frequência:

# E = (h * f) / [exp(h * f / kT) - 1]

# Onde:

#     h é a constante de Planck (6,626 x 10^-34 J.s)
#     f é a frequência (6 x 10^14 Hz)
#     k é a constante de Boltzmann (1,38 x 10^-23 J/K)
#     T é a temperatura em Kelvin (6000 K)

# Substituindo os valores na fórmula, temos:

# E = (6,626 x 10^-34 J.s * 6 x 10^14 Hz) / [exp(6,626 x 10^-34 J.s * 6 x 10^14 Hz / (1,38 x 10^-23 J/K * 6000 K)) - 1]

# E = 6,640 x 10^-20 J

# Portanto, a energia média da radiação emitida por um corpo negro a uma temperatura de 6000 K e
# frequência de 6 x 10^14 Hz é de 6,640 x 10^-20 J.


h = 6.626*(10**-34)

f = 6*(10**14)

e = 2.71828182

k = 1.38*(10**-23)

t = 6000

hv = h*f
kt = k*t

print(hv)
print(kt)
print(hv/kt)

print(hv  / (e**(hv/kt) - 1))
