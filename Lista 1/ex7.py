'''
Escreva um programa que converta um intervalo de tempo dado em segundos para horas, minutos e
segundos. Por exemplo, se o tempo dado for 3.850 segundos, o programa deve fornecer 1h 4min 10s
'''

def exibirHora(valor_segundos):
    tempo_segundos = valor_segundos/60 - int(valor_segundos/60)
    tempo_minutos =  int(valor_segundos/60) - 60
    tempo_horas = int(valor_segundos/3600)

    print("O valor em segundos foi {} e a hora é: {}h {}min {:.2f}s".format(valor_segundos,tempo_horas,tempo_minutos,tempo_segundos))


valor_segundos = int(input("Informe o intervalo de tempo em segundos"))


exibirHora(valor_segundos)
