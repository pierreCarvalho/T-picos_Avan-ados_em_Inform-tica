'''
Implementar  um  algoritmo  para  transpor  matrizes  N x M.  
Transpor  uma  matriz  significa  transformar suas linhas em colunas e vice-versa.
'''

l1 = int(input("Informe a linha da matriz A:")) 
c1 = int(input("Informe a coluna da matriz A:"))

matriz = []
mT = []
for i in range(l1):
    linha = []
    for j in range(c1):
        linha.append(int(input("Informe o valor")))
    matriz.append(linha)

print(matriz)
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz)):
        linha.append(matriz[j][i])
    mT.append(linha)

for linha in mT:
    for valor in linha:
        print(valor,end='\t')
    print()