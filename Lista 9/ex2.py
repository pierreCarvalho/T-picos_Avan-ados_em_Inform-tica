#Mostrar os números de n até 0 (ordem decrescente), em que n é informado pelo usuário

def exibirValor(limite_n):
    if limite_n == 0:
        print(limite_n)
        return 0
    else:
        print(limite_n)
        limite_n -= 1
        return exibirValor(limite_n)


limite_n = int(input("Informe um valor para o N:"))
print("Os números serão mostrados de {} até 0 de forma decrescente".format(limite_n))

exibirValor(limite_n)

