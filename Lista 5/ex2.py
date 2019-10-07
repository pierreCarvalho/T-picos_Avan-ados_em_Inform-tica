'''
Faça um programa que leia uma estrutura composta V de 10 posições e, após, verifique se um
número N, fornecido pelo usuário, existe na estrutura. Se existir, indicar a(s) posição(ões), senão
escrever a mensagem "O número fornecido não foi encontrado!".
'''

tupla = (1,2,3,4,5,6,7,8,9,10)

numero_usuario= int(input("Tente advinhar um número que está na estrutura"))

if numero_usuario in tupla:
    print("Acertou!!")
    print("A sua posição é {} na estrutura".format(tupla.index(numero_usuario)))
else:
    print("O número fornecido não foi encontrado")