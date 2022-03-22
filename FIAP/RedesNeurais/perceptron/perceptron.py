'''
Dada uma rede neural de uma camada cujas entradas (x1,x2 e x3) são respectivamente 1,2 e 3
e os pesos (w1,w2 e w3) sao respectivamente 0.1, 0.2 e 0.3, calcule a saida desse perceptron considerando
uma funcao de ativaco degrau e bias=0

u=x.w + b
f(u) = 1, se u>=0|0

'''
from func import *

x = [1,2,-3]
w = [0.1,0.2,0.3]
b = 0

u = soma_ponderada(x,w,b)
out = funcao_degrau(u)

print("Para os parametros de entrada (x e w),\
o neuronio{0} foi ativado, pois ({1:.2f})={2}"\
.format("" if out == 1 else " não", u, out))
print(out)