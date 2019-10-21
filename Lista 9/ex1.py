#Calcular a soma dos n primeiros números inteiros maiores que zero
def somaInteiros(inicio,limite):
    if inicio == limite:
        return 0
    else:
        inicio +=1
        return inicio + somaInteiros(inicio,limite)


print(somaInteiros(0,5))