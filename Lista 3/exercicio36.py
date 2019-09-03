'''
Escreva o código fonte de um programa que mostre o valor de 
y
 na seguinte função: 
y = 4x + 3.
Solicite ao usuário informar o intervalo de variação do 
x
. 
'''

valor_inicial = int(input("Informe o valor inicial de x"))
valor_final = int(input("Informe o valor final de x"))
print("Na equação: y = 4x + 3")
for i in range(valor_inicial,valor_final+1):
    calculo = (4*i) + 3
    print(" {} ".format(calculo))

