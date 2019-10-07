'''
Implementar  um  programa  para  somar  matrizes,  lembre-se  de  que  as  matrizes 
obrigatoriamente devem ter a mesma dimensão.
'''


l1 = int(input("Informe a linha da matriz A:")) 
c1 = int(input("Informe a coluna da matriz A:"))

l2 = int(input("Informe a linha da matriz B:")) 
c2 = int(input("Informe a coluna da matriz B:"))

matrizA = []
for i in range(l1):
    linha = []
    for j in range(c1):
        linha.append(int(input("Informe o valor para matriz A:")))
    matrizA.append(linha)

matrizB = []
for i in range(l2):
    linha = []
    for j in range(c2):
        linha.append(int(input("Informe o valor para a matriz B:")))
    matrizB.append(linha)

print(matrizA)
print(matrizB)

matrizResultado = []
if len(matrizA) == len(matrizB) and len(matrizA[0]) == len(matrizB[0]):
    print("A soma pode ser feita!")
    for i in range(len(matrizA)):
        linha = []
        for j in range(len(matrizA[0])):
            linha.append(matrizA[i][j] + matrizB[i][j])
        matrizResultado.append(linha)

    print(matrizResultado)
else:
    print("Não pode ser feita!")
