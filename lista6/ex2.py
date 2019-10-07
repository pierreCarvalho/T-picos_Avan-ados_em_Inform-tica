#Escreva  um  programa  que  leia  uma  palavra  qualquer  e verifica  se  esta  palavra  é  um palíndromo


palavra = input("Digite uma palavra qualquer:")


if(palavra == palavra[::-1]):
    print("É um palindromo!")
else:
    print("Não é ")
