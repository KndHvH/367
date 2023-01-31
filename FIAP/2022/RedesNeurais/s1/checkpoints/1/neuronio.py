from sup import *

'''3.	Um neurônio recebe 4 entradas cujos valores são iguais a 25, -19, 4 e -3. 
Os respectivos pesos são 0,8, 0,3, -1,1 e -0,9. Calcule a saída do neurônio para as 
situações abaixo. Você pode calcular na mão ou via código Python. Em qualquer caso,
 mostre ou um print do código ou o raciocínio dos cálculos:
a.	O neurônio é linear. Assuma um bias igual a 0,1; 
b.	O neurônio é baseado na função de ativação degrau. Assuma um bias igual a 0,4;
'''


w = [0.0,0.0,0.0,0.0]
b = 0

u = soma_ponderada(x,w,b)

exit = funcao_degrau(u)

print(exit)