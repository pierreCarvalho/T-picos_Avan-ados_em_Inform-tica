#A operação de potenciação pode ser resolvida de forma iterativa ou de forma recursiva.
# Desenvolva a função recursiva para o cálculo da potência de um número.
# numero = 2
# potencia = 3
# resultado = 8

def potenciarValor(numero,potencia,i):
    if i > potencia:
        return 1
    else:       
        i += 1
        return numero * potenciarValor(numero,potencia,i)

i = 1
numero = int(input("Informe um numero inteiro:"))
potencia = int(input("Informe a potencia:"))
resultado = potenciarValor(numero,potencia,i)
print("A potencia do numero ",resultado)