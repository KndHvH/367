# Constante de Stefan-Boltzmann
sigma = 5.67e-8 # W/m^2K^4

# Área do corpo negro em metros quadrados
A = 10

# Temperatura do corpo negro em Kelvin
T = 500

# Tempo em segundos
t = 3600

# Energia total emitida pelo corpo negro em Joules
E = sigma * A * T**4 * t

print("A energia total emitida pelo corpo negro é de", E, "Joules.")
