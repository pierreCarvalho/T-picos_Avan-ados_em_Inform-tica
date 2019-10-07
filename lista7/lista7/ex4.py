'''
Faça um programa que leia uma matriz e, armazene a i-ésima linha da matriz em um vetor. 
As dimensões da matriz e a linha a  ser armazenada são informadas pelo usuário.
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

vetor = []
linha = (int(input("Informe a linha da matriz que quer armazenar em um vetor:")))
if linha < len(matriz):
    vetor.append(matriz[linha])
    print(vetor)
else:
    print("Fora do alcance!")


