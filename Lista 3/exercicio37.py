'''
Faça  um  programa  que  leia  números  inteiros  até  que  seja  informado  um  número  negativo. 
Escreva o menor número ímpar informado (desconsiderando o número negativo). Se não tiver 
sido informado nenhum número ímpar, o programa deve escrever uma mensagem informando 
que nenhum número ímpar foi informado.
'''
numero_impar = 0
while True:
    numero = int(input("digite um valor"))
    if numero % 2 == 1:
        numero_impar = numero
        if numero < 0:
            print("Numero negativo!")
            break
    elif numero < 0:
        print("Numero negativo!")
        break
print(numero_impar)