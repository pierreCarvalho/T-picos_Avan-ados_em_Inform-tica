'''
Fazer um  programa  que  leia  duas matrizes  inteiras  de  ordem  4 e  verifique  se  a  soma  dos 
elementos das diagonais principais são iguais.
'''
from random import randint

matrizA = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(randint(0,9))
    matrizA.append(linha)

matrizB = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(randint(0,9))
    matrizB.append(linha)

print("Matriz A:")
for linha in matrizA:
    for valor in linha:
        print(valor,end='\t')
    print()

print("Matriz B:")
for linha in matrizB:
    for valor in linha:
        print(valor,end='\t')
    print()    

soma1 = 0
soma2 = 0
for i in range(4):
    soma1 = soma1 +  matrizA[i][i]
    soma2 = soma2 + matrizB[i][i]

if soma1 == soma2:
    print("As somas dos elementos são iguais!")
else:
    print("Não são iguais {} , {}".format(soma1,soma2))