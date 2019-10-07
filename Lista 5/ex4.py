'''
Faça um programa que leia um número indeterminado de notas de uma turma, a entrada de notas
deve encerrar quando a nota informada for igual a -1 (que não deve ser armazenado). Após esta
entrada de dados, faça:
(a) Mostre a quantidade de valores que foram lidos;
(b) Exiba todos os valores na ordem em que foram digitados;
(c) Exiba todos os valores na ordem inversa;
(d) Calcule e mostre a soma dos valores;
(e) Calcule e mostre a média dos valores;
(f) Calcule e mostre a quantidade de valores acima da média calculada;
(g) Calcule e mostre a quantidade de valores abaixo de determinado valor de referência,
    que deve ser informado.
'''

lista_notas = []
flag = True
while flag:
    nota = int(input("Digite uma nota de um aluno:"))
    if nota == -1:
        flag = False
    else:
        lista_notas.append(nota)
        

print("A quantidade de notas que foram lidas foi de {}".format(len(lista_notas)))
print("Notas na ordem que foram inseridas \n {}".format(lista_notas))
print("Notas na ordem inversa que foram inseridas \n {}".format(lista_notas[::-1]))
soma = 0
for i in range(len(lista_notas)):
    soma += lista_notas[i]
media = soma/len(lista_notas)
print("A soma das notas foi de {}".format(soma))
print("A soma das notas foi de {}".format(media))
for i in range(len(lista_notas)):
    if lista_notas[i] > media:
        print("O valor {} é maior que a média".format(lista_notas[i]))

valor_referencia = int(input("Informe um valor de referencia:"))

for i in range(len(lista_notas)):
    if lista_notas[i] < valor_referencia:
        print("O valor {} é menor que o valor de referência".format(lista_notas[i]))
