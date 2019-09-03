'''
Escreva um programa que receba o valor da quantia solicitada e retorne
a distribuição das notas de acordo com este critério:
Considere que a máquina possui notas de R$100, R$50, R$20, R$10, R$5 e R$2.
Nesse caso, um saque de R$139 resultaria em 1 nota de R$100, 1 nota de R$20, 1 nota de R$10, 1 nota de R$5 e 2 notas de R$2.
'''
def sacar(valor):
    n_100 = 0
    n_50 = 0
    n_20 = 0
    n_10 = 0
    n_5 = 0
    n_2 = 0
    while(valor):
        if valor >= 100:
            print("maior que 100")
            n_100 = n_100 + 1
            valor = valor - 100
        elif valor >= 50:
            print("maior que 50")
            n_50 = n_50 + 1
            valor = valor - 50
        elif valor >= 20:
            print("maior que 20")
            n_20 = n_20 + 1
            valor = valor - 20

        elif valor >= 10:
            print("maior que 10")
            n_10 = n_10 + 1
            valor = valor - 10

        elif valor >= 5:
            print("maior que 5")
            n_5 = n_5 + 1
            valor = valor - 5
        elif valor >= 2:
            print("maior que 2")
            n_2 = n_2 + 1
            valor = valor - 2

    print("O resultado do saque foi de: {} notas(s) de R$100,{} nota(s) de 50, {} nota(s) de R$20, {} nota(s) de R$10, {} nota(s) de R$5 e {} nota(s) de R$2.".format(n_100,n_50,n_20,n_10,n_5,n_2))

valor = float(input("Informe o valor para sacar"))

sacar(valor)
