# Para calcular a energia de um fóton com uma frequência de 5x10^14 Hz, 
# podemos usar a fórmula E = nhv, onde E é a energia do fóton, n é o número de fótons, 
# h é a constante de Planck e v é a frequência.

# Substituindo os valores conhecidos na fórmula, temos:

# E = (1)(6.626 x 10^-34 J.s)(5 x 10^14 Hz)
# E = 3.313 x 10^-19 J

# Portanto, a energia do fóton é de 3.313 x 10^-19 Joules.


Ef = ''

h = 6.626*(10**-34)

f = 5*10**14

if Ef == '':
    Ef = h*f

if f == '':
    f = Ef/h

print(Ef)
print(h)
print(f)