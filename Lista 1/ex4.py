'''
Um motorista de taxi deseja calcular o rendimento de seu carro na praça. Escreva um algoritmo
para ler o valor do combustível, a marcação do odômetro no início do dia, a marcação no final do dia,
o número  de  litros  de  combustível  gasto  e  o  valor  total  (R$)  recebido  dos  passageiros.  Calcular
escrever a média do consumo em Km/l e o lucro líquido do dia.
'''

def calcularMediaConsumo(distancia,litros):
    return distancia/litros

def calcularLucroLiquido(total_gasto,total_ganho):
    return total_ganho - total_gasto

valor_combustivel = float(input("Valor do combustível"))
marcacao_odometro_inicial = int(input("Marcação do odômetro no inicio do dia"))
marcacao_odometro_final = int(input("Marcação do odômetro no final do dia"))
numero_litros = float(input("Numero de litros de combustível gasto"))
valor_passageiros = float(input("Valor total recebido dos passageiros"))

distancia_percorrida = marcacao_odometro_final - marcacao_odometro_inicial
combustivel_gasto = valor_combustivel * numero_litros

media_consumo = calcularMediaConsumo(distancia_percorrida,numero_litros)
lucro = calcularLucroLiquido(combustivel_gasto,valor_passageiros)

print("O lucro liquido do dia foi de {} reais".format(lucro))
print("A média de consumo foi de {} km/l".format(media_consumo))