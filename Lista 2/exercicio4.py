'''
Considere  a  tabela  de  Alíquota  de  Imposto  de  Renda  (IR)  a  seguir.  Desenvolva  um
algoritmo para ler um valor de salário mensal, mostrar o % da alíquota do imposto de Renda
e o valor em R$ da alíquota.
'''


salario_mensal = float(input("Informe o salário mensal:"))

if salario_mensal <= 1566.61:
    print("não possui porcentagem da aliquota, o valor em R$ é: {} ".format(salario_mensal))
elif salario_mensal >= 1566.62  and salario_mensal <= 2347.85:
    print("A porcentagem da aliquota é de 7.5% e o valor em R$ é: {}".format(salario_mensal*7.5))
elif salario_mensal >= 2347.86  and salario_mensal <= 3130.51:
    print("A porcentagem da aliquota é de 15.0% e o valor em R$ é: {}".format(salario_mensal*15.0))
elif salario_mensal >= 3130.52  and salario_mensal <= 3911.63:
    print("A porcentagem da aliquota é de 22.5% e o valor em R$ é: {}".format(salario_mensal*22.5))
elif salario_mensal >= 3911.64:
    print("A porcentagem da aliquota é de 27,5% e o valor em R$ é: {}".format(salario_mensal*27.5))