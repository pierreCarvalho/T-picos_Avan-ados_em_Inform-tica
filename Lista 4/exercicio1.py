#Escreva um programa que leia e mostre em uma estrutura composta 20 elementos inteiros. A 
#seguir, conte quantos valores pares existem.

lista = []
conta_pares = 0
for i in range(20):
    lista.append(i+1)
print("A lista é",lista[:])
for i in range(len(lista)):
    if lista[i] %  2 == 0:
        conta_pares += 1
print("Há ",conta_pares," pares")
