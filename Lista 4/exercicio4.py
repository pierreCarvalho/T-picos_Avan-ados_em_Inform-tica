'''
Ler e armazenar 30 elementos inteiros em uma estrutura com
posta. Encontre e mostre o menor
elemento e a sua posição
'''

lista = []

for i  in range(5):
    valor1 = int(input("Informe valor para a lista A: "))
    lista.append(valor1)
menor = lista[i]
for i in range(len(lista)):
    if lista[i] < menor:
        menor = lista[i]       
print("O menor valor é: ",menor)
print("A sua posição é: {} ".format(lista.index(menor)))
