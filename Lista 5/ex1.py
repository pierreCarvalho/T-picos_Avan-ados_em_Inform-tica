'''
Escrever um programa que armazene 10 valores inteiros em duas estruturas X(10) e Y(10). Crie,
a seguir, uma terceira estrutura Z, que seja:
(a) A união de X com Y
(b) A diferença entre X e Y
(c) A soma entre X e Y
(d) O produto entre X e Y
(e) A interseção entre X e Y
Escreva Z a cada operação.
'''
import random as randint

def gerarNumeros(conjunto):
    while len(conjunto) < 5:
        valor = randint.randint(0,10)
        conjunto.add(valor)
    return conjunto

x = set()
y = set()
z = set()
x = gerarNumeros(x)
y = gerarNumeros(y)
print("Estrutura x: {}".format(x))
print("Estrutura y: {}".format(y))

z = x.union(y)
print("A  união entre as estruturas x e y é: {}".format(z))
z = x.symmetric_difference(y)
print("A diferença entre as estruturas x e y é: {}".format(z))
z = x.intersection(y)
print("A interseção entre as estruturas x e y é: {}".format(z))