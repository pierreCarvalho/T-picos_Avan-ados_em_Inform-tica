flag = True
n = int(input("Informe o n para o cubo:"))
c_magico = (n * (n*n + 1)) / 2
#esse numero tem que variar de 1 à (n*n)
print("A constante é: ",c_magico)
print("Os valores poderão ir de 1 à {}".format(n*n))
print(input("Tecle algo para continuar...."))

#inicializando a matriz com 0
matriz = []
for i in range(n):
    matriz.append([0]*n)
# para criar a matriz, a formula é
# um para cima, um para o lado
pos_inicial = int( ((n+1) / 2) -1)
valor = 1
#colocando o 1 na posição do meio na matriz
matriz[0][pos_inicial] = valor
valor += 1
#posicao inicial
linha = 0
coluna = pos_inicial
pos_atual_valor = [linha,coluna]

while flag:
    print(matriz)
    #formula cima e direita
    linha = pos_atual_valor[0] - 1
    coluna = pos_atual_valor[1] + 1
    if linha == -1 and coluna == n:
        #se ja tiver um numero, coloca  embaixo da posicao anterior
        pos_anterior = [linha + 1, coluna - 1]
        matriz[(pos_anterior[0]+1)][pos_anterior[1]] = valor       
        #seta a posicao do valor
        pos_atual_valor[0] = (pos_anterior[0]+1)
        pos_atual_valor[1] = pos_anterior[1]
    elif linha == - 1:
        #continua na mesma coluna mas desce até o final da linha
        matriz[n-1][coluna] = valor  
        #agora que estamos no 2, a gente seta a posicao para a posicao do 2
        pos_atual_valor[0] = n-1
        pos_atual_valor[1] = coluna
    elif coluna == n:
        #continua na mesma linha mas vai na coluna inicial
        matriz[linha][0] = valor
        #seta a nova posivao do valor
        pos_atual_valor[0] = linha
        pos_atual_valor[1] = 0    
    elif matriz[linha][coluna] != 0:
        #se ja tiver um numero, coloca  embaixo da posicao anterior
        pos_anterior = [linha + 1, coluna - 1]
        matriz[(pos_anterior[0]+1)][pos_anterior[1]] = valor      
        #seta a posicao do valor
        pos_atual_valor[0] = (pos_anterior[0]+1)
        pos_atual_valor[1] = pos_anterior[1]   
    else:
        #se não cair em nenhuma das regras, cai no normal!
        matriz[linha][coluna] = valor
        pos_atual_valor[0] = linha
        pos_atual_valor[1] = coluna   
    #atualiza a posicao do valor atual
    valor += 1
    if valor > n*n:
        flag = False
    

print("----------Matriz final----------")
for linha in matriz:
    for valor in linha:
        print(valor,end='\t')
    print()