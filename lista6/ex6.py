#Ler uma palavra e uma letra qualquer. Mostrar a palavra cortada na primeira posição em que
#encontrar a letra informada.

palavra1 = input("Digite uma palavra qualquer: ")
letra1 = input("Digite uma letra qualquer: ")
pos = palavra1.find(letra1)
print(palavra1[:pos])
