'''
Faça um algoritmo para ler dois números inteiros que representam um intervalo de valores. Ler 
um valor que representa um expoente. Calcular e mostrar o valor resultante se elevarmos cada 
um dos números do intervalo à potência informada. 
'''

valor_inicial = int(input("Informe o valor inicial para o intervalo:"))
valor_final = int(input("Informe o valor final para o intervalo:"))
expoente = int(input("Informe o valor para o expoente:"))
for i in range(valor_inicial,valor_final+1):
    print("{}".format(i**expoente))
    