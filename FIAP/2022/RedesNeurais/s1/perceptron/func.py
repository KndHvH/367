def soma_ponderada(x,w,b):
    soma=0
    for i in range(len(x)):
        soma+=x[i]*w[i]
    return soma + b

def funcao_degrau(u):
    if u >= 0:
        return 1
    return 0

