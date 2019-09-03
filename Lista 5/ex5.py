'''
Escreva um programa que lê duas notas de vários alunos e armazena esses dados em um
dicionário, no qual o nome do aluno corresponde a chave. A entrada de dados deve terminar
quando for informado um nome igual a um determinado valor, definido pelo programador. O
programa deve receber o nome do aluno e retornar sua média correspondente.
'''

dic_alunos = {}
while True:
    nome = input("Informe o nome de um aluno: ")
    if nome == '5':
        print("Valor invalido")
        break
    nota1 = float(input("Informe a nota 1 do aluno  "))
    nota2 = float(input("Informe a nota 1 do aluno  "))
    media = (nota1+nota2) /2
    #no dicionario adiciona na chave nome o valor da média
    dic_alunos[nome] = media

print(dic_alunos)

while True:
    nome = input("Informe o nome do aluno desejado: ")
    if nome in dic_alunos:  
        print("A média do {} é: {}".format(nome,dic_alunos[nome]))