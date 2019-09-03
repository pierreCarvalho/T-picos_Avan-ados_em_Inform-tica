#Faça um algoritmo para ler um valor numérico e calcular e escrever o seu fatorial. 
#n . (n – 1) . (n – 2) . (n – 3)!
valor = int(input("Informe um valor para calcular o seu fatorial:"))
fat = 1
i = 2

while i <= valor:
    fat = fat * i
    i = i+1
print(fat)

for i in range(2,valor+1):
    fat = fat * i

print(fat)


