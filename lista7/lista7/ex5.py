'''
Faça  um  programa  que  leia  uma  matriz  e  encontre  a  linha  que  possui  a  menor  soma.  Se houver
empate informe todos os valores das linhas que obtiveram a menor soma.
'''

l1 = int(input("Informe a linha da matriz A:")) 
c1 = int(input("Informe a coluna da matriz A:"))
matriz =[]
for i in range(l1):
    linha = []
    for j in range(c1):
        linha.append(int(input("Informe o valor")))
    matriz.append(linha)

print("Matriz A:")
for linha in matriz:
    for valor in linha:
        print(valor,end='\t')
    print()

somaMenor = 599
listaIndices = []
for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz[0])):
        soma = soma + matriz[i][j]

    if soma < somaMenor:
        somaMenor = soma
        listaIndices.append(i)

if len(listaIndices) > 1:
    for i in range(len()):
        print(matriz[listaIndices[i]])


print("A linha {} tem como soma {}".format(listaIndices[0],somaMenor))
