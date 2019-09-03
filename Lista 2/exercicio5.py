'''
Escreva  um  algoritmo  que  leia  a  altura  (em  metros),  o  peso  (em  quilogramas)  e  o  sexo
(M ou F) e calcule o peso ideal, dado por:
Peso ideal do homem = (72,7 * altura) – 58
Peso ideal da mulher = (62,1 * altura) – 44, 7.
O algoritmo deve informar também se a pessoa está abaixo ou acima de seu peso ideal e em
quantos quilos.

'''
altura = float(input("Informe a sua altura"))
peso = float(input("Informe o seu peso"))
escolha = input("Informe o seu sexo: masculino ou feminino")

if escolha == 'masculino':
    resultado = (72.7 * altura) - 58
    print("masculino")

    #if()
elif escolha == 'feminino':
    print("feminino")
    resultado = (62.1 * altura) - 44.7