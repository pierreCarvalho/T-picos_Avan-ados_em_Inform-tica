'''
Escreva um programa que armazene em uma estrutura composta 50 números inteiros e mostre
somente os positivos
'''
lista = []
for i in range(5):
    valor = int(input("Informe valor"))
    lista.append(valor)

for i in range(len(lista)):
    if lista[i] > 0:
        print("",lista[i])