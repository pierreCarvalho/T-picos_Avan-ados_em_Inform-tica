#Gerar a sequência números ímpares positivos, até um número n informado pelo usuário

def exibirImpares(inicio,limite_n):
    if inicio == limite_n:
        if inicio % 2 == 1:
            print(inicio)
        return 0
    else:
        if inicio % 2 == 1:
            print(inicio)
        inicio += 1
        return exibirImpares(inicio,limite_n)


limite_n = int(input("Informe um valor para o limite da recursão:"))
print("Numeros impares:")
exibirImpares(0,limite_n)