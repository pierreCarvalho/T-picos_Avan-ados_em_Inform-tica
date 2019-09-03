'''
Escreva  um  algoritmo  que  lê  três  valores  para  os  lados  de  um  triângulo  (cada  lado  do
triângulo deve ser menor que a soma dos outros dois lados). O programa deve verificar se os
lados  fornecidos  formam  realmente  um  triângulo,  e  caso  esta  condição  seja  verda
deira,  se  o triângulo  é  equilátero  (todos  lados  iguais),  isósceles  (dois  lados  iguais)  ou  escaleno  (todos
lados diferentes

'''

a = int(input("Informe o lado A do triangulo"))
b = int(input("Informe o lado B do triangulo"))
c = int(input("Informe o lado C do triangulo"))


if a < b+c or b < a+c or c < a+b :
    print("O triangulo é valido")
    if a == b and a == c:
        print("O triangulo é equilátero")
    elif a == b or b == c or a == c:
        print("O triangulo é isósceles")
    else:
        print("Os lados são diferentes!")