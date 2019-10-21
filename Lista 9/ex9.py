#6. A sequência [0, 1, 1, 2, 3, 5, 8, 13, 21, 34...] é conhecida como Sequência ou Série
# de Fibonacci. Defina a sequência recursivamente e a implemente em uma função.


def sequenciaFibonnaci(valor):
    if valor > 50:
        return 0
    else:
        print(valor)
        prox_valor = valor + (valor+1)
        return valor + sequenciaFibonnaci(prox_valor)

sequenciaFibonnaci(0)
