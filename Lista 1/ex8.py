'''
Considere um sistema de equações lineares que é representado da seguinte forma:
{ Ax + By = C
{ Dx + Ey = F
Uma possível solução para o sistema é utilizar as sequintes equações:
x = CE - BF / AE - BD
y = AF - CD / AE - BD
Escreva um algoritmo para ler o conjunto de coeficientes (A, B, C, D, E e F) e imprimir a solução,
ou seja, os valores de x e y.

Existem casos para os quais o algoritmo não funciona?
'''

def calcularX(coef_A,coef_B,coef_C,coef_D,coef_E,coef_F):

    if((coef_C * coef_E) == (coef_B * coef_F) or (coef_A * coef_E) == (coef_B *coef_D) ):
        print("Opa, troque os valores dos coeficientes para calcular o x!")
        return 0
    x = ((coef_C * coef_E) - (coef_B * coef_F)) /((coef_A * coef_E) - (coef_B *coef_D))
    return x

def calcularY(coef_A,coef_B,coef_C,coef_D,coef_E,coef_F):

    if((coef_A * coef_F) == (coef_C * coef_D) or (coef_A * coef_E) == (coef_B *coef_D) ):
        print("Opa, troque os valores dos coeficientes para calcular o y!")
        return 0
    y = ((coef_A * coef_F) - (coef_C * coef_D)) / ((coef_A * coef_E) - (coef_B *coef_D))
    return y


coef_A = int(input("Informe o valor de A"))
coef_B = int(input("Informe o valor de B"))
coef_C = int(input("Informe o valor de C"))
coef_D = int(input("Informe o valor de D"))
coef_E = int(input("Informe o valor de E"))
coef_F = int(input("Informe o valor de F"))


valor_x = calcularX(coef_A,coef_B,coef_C,coef_D,coef_E,coef_F)
valor_y = calcularY(coef_A,coef_B,coef_C,coef_D,coef_E,coef_F)
print(valor_x)

