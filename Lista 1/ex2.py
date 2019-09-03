'''
Escrever  um  algoritmo  para  ler  as  dimensões  de  uma  cozinha  (comprimento,  largura  e  altura),
calcular e escrever a quantidade de caixas de azulejos para azulejar todas as paredes (considere que
não será descontada a área ocupada por portas  e  janelas). Cada  caixa de  azulejos possui 1,5 metros
quadrados
'''

print("Digite as dimensões de uma cozinha")

comprimento = float(input("Comprimento"))
largura = float(input("largura"))
altura = float(input("altura"))
caixa_azulejo = 1.5

area_parede = (2*altura*largura) + (2*altura*comprimento)
print(area_parede)

quantidade_azulejos = area_parede/caixa_azulejo

print(quantidade_azulejos)





