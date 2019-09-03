for i in range(1000,10000):
    resultado = i // 100
    rest = i % 100
    soma = rest +resultado
    valor3 = soma ** 2
    if valor3 == i:
        print("Numero válido {} = {}".format(valor3,i))
