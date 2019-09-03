'''
Escrever um algoritmo
o para ler o valor da mensalidade e o percentual de reajuste. Calcular e mostrar
o novo valor da mensalidade com o reajuste
'''
mensalidade = float(input("Digite o valor da mensalidade"))
porcentagem_reajuste = float(input("digite a porcentagem do reajuste na mensalidade"))

reajuste = mensalidade + ( (porcentagem_reajuste * mensalidade) / 100)

print(mensalidade)
print(porcentagem_reajuste)
print("o reajuste ficou: {}".format(reajuste))


