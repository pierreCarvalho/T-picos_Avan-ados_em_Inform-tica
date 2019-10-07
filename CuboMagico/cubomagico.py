#regra para a inserção dos numeros
# Defina a casa 1 como sendo a do meio da linha superior
# Você deve sempre preencher o número em sequência (1, 2, 3, 4 etc.),
# um para cima e um para direita
#condições:
#  - Se a sequência terminar uma "casa" acima da fileira superior do quadrado mágico,
#        continue nessa fileira, mas defina o número na fileira inferior dessa coluna.
#  - Se a sequência terminar uma "casa" à direita da coluna mais à direita do quadrado mágico,
#        continue nela, mas defina o número na coluna mais à esquerda dessa fileira.
#  - Se a sequência terminar em uma casa já numerada, volte para a última casa que já
#        foi numerada e defina o próximo número na casa diretamente abaixo dessa
from random import randint
n = int(input("Informe o n para o cubo:"))
c_magico = (n * (n*n + 1)) / 2
#esse numero tem que variar de 1 à (n*n)
valor = 1


print("A constante é: ",c_magico)
print("Os valores poderão ir de 1 à {}".format(n*n))
print(input("Tecle algo para continuar...."))
#o tamanho da matriz será de acordo com o numero N



#par impar par
#impar impar impar
flag = True
while flag:
    matriz = []
    numeros = []
    for i in range(n*n):
        numeros.append(i+1)

    for i in range(n):
        linha = []
        for j in range(n):
            valor = numeros[randint(0,(len(numeros)-1))]
            linha.append(valor)
            numeros.remove(valor)
        matriz.append(linha)
    contador = 0
    #verifica a soma das linhas
    for i in range(n):
        valor = 0
        for j in range(n):
            valor += matriz[i][j]
        if(valor == c_magico):
            #print("A linha {} passou".format(i))
            contador += 1
            if contador == 3:
                print(matriz)
                flag = False

    p#verifica a soma das colunas
    for i in range(n):
        valor = 0
        for j in range(n):
            valor += matriz[j][i]
        if(valor == c_magico):
            #print("A coluna {} passou".format(j))
            contador += 1
            if contador == 6:
                
                flag = False
    
   
        