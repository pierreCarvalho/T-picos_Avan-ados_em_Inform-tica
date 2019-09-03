'''
Considerando que com um galão com 5 litros de tinta é possível pintar até 2 metros quadrados. Faça
um algoritmo que leia a altura e a largura de uma parede, calcule e escreva a quantidade de galões de
tinta necessários e o preço total para adquirir a tinta
'''

def calcularQuantidade(area):
    return (5*area) / 2

def calcularValorTotal(quantidade_tinta):
    return (quantidade_tinta * 130) / 5

largura = int(input("Digite a largura de sua parede:"))
altura = int(input("Digite a altura de sua parede:"))

area = largura * altura

quantidade_tinta = calcularQuantidade(area)

valor_total = calcularValorTotal(quantidade_tinta)

print("A quantidade de galões de tinta com 5 litros será {} e o valor total é de {} reais".format(quantidade_tinta,valor_total))