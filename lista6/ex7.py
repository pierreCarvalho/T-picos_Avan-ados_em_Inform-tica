#Ler uma palavra e duas letras, toda vez que a primeira letra aparecer substituí-la pela segunda.
#Apresentar a como resultado a nova palavra.


palavra1 = input("Digite uma palavra qualquer: ")
letra1 = input("Digite uma letra qualquer: ")
letra2 = input("Digite uma letra qualquer: ")

palavra1 = palavra1.replace(letra1,letra2)
print(palavra1)