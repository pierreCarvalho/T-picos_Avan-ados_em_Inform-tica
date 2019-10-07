#Escreva um programa que leia uma palavra qualquer e conte o número de vogais


palavra = input("Digite uma palavra qualquer:")
contar = 0

palavra = palavra.lower()

for i in palavra:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' ):
        contar += 1


print("Quantidade de vogais é: ",contar)