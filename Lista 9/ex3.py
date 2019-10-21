#Mostrar os números de 0 até n (ordem crescente), em que n é informado pelo usuário.
def exibirValor(inicio,limite_n):
    if inicio == limite_n:
        print(inicio)
        return 0
    else:
        print(inicio)
        inicio += 1
        return exibirValor(inicio,limite_n)


limite_n = int(input("Informe um valor para o N:"))
print("Os números serão mostrador de 0 até {} de forma crescente".format(limite_n))

exibirValor(0,limite_n)