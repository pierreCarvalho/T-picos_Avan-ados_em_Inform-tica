'''
Escrever um algoritmo para ler o número de eleitores de um município, o número de votos brancos,
nulos  e  validos.  Calcular  e  escrever  o  percentual  que  cada
um  representa  em  relação  ao  total  de eleitores.
'''


votos_validos = int(input("Digite os votos validos"))
votor_nulos = int(input("Digite os votos nulos"))
votos_brancos = int(input("Digite os votos brancos"))

total = votor_nulos+votos_brancos+votos_validos

percentual_validos = (votos_validos * 100) / total
percentual_nulos = (votor_nulos * 100) / total
percentual_brancos = (votos_brancos * 100) / total

print("O percentual dos votos brancos, nulos e válidos é: {} {} {}".format(percentual_brancos,percentual_nulos,percentual_validos))

