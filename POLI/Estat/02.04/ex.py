import numpy as np

# Dados de exemplo
X = np.array([[1, 2], [3, 4], [5, 6]])

# Calcular a matriz de covariância
cov_matrix = np.cov(X, rowvar=False)

print(cov_matrix)