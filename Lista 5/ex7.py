'''
Ler os dados de “N” pessoas (nome, sexo, idade e saúde)
A leitura dos dados deve encerrar a
entrada do nome informado for igual a

O programa deve apresentar como resultado o nome da
pessoa e se ela está apta ou não para cumprir o serviço militar obrigatório no Brasil.

Estão aptos ao serviço militar pessoas do sexo masculino, com 18 anos e sem problemas de saúde. O
resultado também deve mostrar o número total de aptos ao serviço militar
'''

dic_aprovados = {}
flag = True
while flag:
    lista_pessoa = []
    print("Cadastro de pessoa! ")
    nome = input("Informe o nome: ")
    sexo = input("Informe o sexo:")
    idade = int(input("Informe a idade:"))
    saude = input("Problemas de saúde?")
    if nome == 'a':
        flag = False
    elif sexo == 'masculino' and idade >= 18 and saude == 'nao':
        dic_aprovados[nome] = 'Apto para cumprir o serviço militar Brasileiro'

for key in dic_aprovados:
    print("O {} está {}".format(key, dic_aprovados[key]))