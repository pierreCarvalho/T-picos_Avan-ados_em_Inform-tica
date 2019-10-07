'''
Os vendedores de uma loja necessitam identificar rapidamente os preços a partir dos códigos
dos produtos. Faça um programa que, inicialmente, leia e armazene os códigos e os preços de 10
produtos em duas estruturas (uma para os códigos e outra para os preços) e permita consulta
de preços a partir dos códigos.

o que fazer
 - ler e armazenar em uma estrutura codigos de 10 produtos
 - ler e armazenar em uma estrutura preços de 10 produtos
 - permitir a consulta de preços a partir de codigo

 exemplo:  codigo:001, preço :15,4

'''
lista_codigos = []
lista_precos = []
flag = True
for i in range(10):
    codigo = int(input("Informe o código do produto:"))
    preco = float(input("Informe o preço do produto:"))
    lista_codigos.append(codigo)
    lista_precos.append(preco)

while flag:
    codigo_pedido = int(input("Digite o código do produto"))
    if codigo_pedido in lista_codigos:
        posicao = lista_codigos.index(codigo_pedido)
        produto_pedido = lista_precos[posicao]
        print("O preço do codigo {} é {} reais".format(codigo_pedido,produto_pedido))