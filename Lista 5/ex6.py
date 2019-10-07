'''
Escrever um programa que cadastre o nome, a altura, o peso e o cpf de algumas pessoas. Com os
dados cadastrados, em seguida localizar uma pessoas através do seu CPF e imprimir seus dados.
'''

dicionario_geral = {}
flag = True
for i in range(5):
    lista_pessoal = []
    print("Cadastro de pessoa! ")
    nome = input("Informe o nome: ")
    cpf = int(input("Informe o CPF:"))
    altura = float(input("Informe a altura"))
    peso = float(input("Informe o peso:"))
    lista_pessoal.append(nome)
    lista_pessoal.append(altura)
    lista_pessoal.append(peso)
    dicionario_geral[cpf] = lista_pessoal

print(dicionario_geral)
while flag:
    cpf_pedido = int(input("Informe o CPF desejado: "))
    if cpf_pedido in dicionario_geral:
        lista_pessoa = dicionario_geral[cpf_pedido]
        print("A pessoa é {} com altura {} e peso {}".format(lista_pessoa[0],lista_pessoa[1],lista_pessoa[2]))
    else:
        print("CPF inválido")
    
    sair = input("Quer sair ou continuar?")
    if sair == 'sair':
        flag = False
    

