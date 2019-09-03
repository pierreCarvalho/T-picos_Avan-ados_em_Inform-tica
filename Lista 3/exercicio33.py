#Faça um algoritmo para ler dois valores inteiros. O primeiro representa o primeiro elemento de 
#uma progressão aritmética, e o segundo a razão. Calcule e mostre os 10 elementos seguintes. 

primeiro_valor = int(input("Informe um valor"))
razao = int(input("Informe outro valor"))
i = 1
calculo = primeiro_valor
print("numero: ",calculo)
while i < 10:
    calculo += razao      
    i += 1
    print("numero: ",calculo)
