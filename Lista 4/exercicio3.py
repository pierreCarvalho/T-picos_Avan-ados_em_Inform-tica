'''
Escreva um programa que leia duas estruturas (A e B) de 10 posições e faça a multiplicação dos
elementos de mesmo índice, colocando o resultado em uma terceira estrutura (C). Mostre os 
elementos
de C.
'''
lista1 = []
lista2 = []
lista_resultado = []
for i in range(50):
    valor1 = int(input("Informe valor para a lista A: "))
    valor2 = int(input("Informe valor para a lista B: "))
    lista1.append(valor1)
    lista2.append(valor2)

print("Lista A: ",lista1)
print("Lista B: "lista2)

for i in range(50):
    valor = lista1[i] * lista2[i]
    lista_resultado.append(valor)

print("Lista C: "lista_resultado)
