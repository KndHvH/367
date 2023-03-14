# Constante de Stefan-Boltzmann
sigma = 5.67e-8 # W/m^2K^4

# Temperatura em Kelvin
T = 2500

# Potência emitida pela
P = 100

# Área da superfície
A = P / (sigma * T**4)

print("A área da superfície é de", A, "metros quadrados.")
