'''
Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se
dividirmos  o  número  em  dois  números  de  dois  dígitos,  um  composto  pela  dezena  e  pela
unidade, e  outro  pelo milhar e  pela  centena,  se  somarmos  estes  dois  novos  números  gerando
um  terceiro,  o  quadrado  deste  terceiro  número  é  exatamente  o  número  original  de  quatro
dígitos.

Escreva um programa para ler um número e verificar se ele obedece a esta característica
'''

numero = int(input("Informe o valor entre 1000 a 9999"))
if numero < 10000 and numero > 999:
    resultado = numero // 100
    rest = numero % 100
    print(rest)

    soma = rest +resultado
    print(soma)

    numero3 = soma ** 2

    if numero3 == numero:
        print("Numero válido {} = {}".format(numero3,numero))
    elif numero3 > numero:
        print("O número não obede a essa caracteristica {} > {}".format(numero3,numero))
    elif numero3 < numero:
        print("O número não obede a essa caracteristica {} < {}".format(numero3,numero))


else:
    print("Valor inválido!")

