'''
Escrever  um  algoritmo  que  leia  as  coordenadas  cartesianas  de  dois  pontos  no  plano.  Se
traçarmos  apenas  linhas  paralelas  aos  eixos x e y,  estes  dois  pontos  são  suficientes  para
definir  um  retângulo.  Baseado  nisto,  faça  com  que  o  algoritmo  calcule  a  área  do  retângulo.
Lembre - se de que o valor da área não pode ser negativo
'''

x1 = int(input("Informe o x do ponto 1"))
y1 = int(input("Informe o y do ponto 2"))

x2 = int(input("Informe o x do ponto 2"))
y2 = int(input("Informe o y do ponto 2"))




if(x1 < x2 and y1 < y2 or x1 > x2 and y1 > y2 ):
    print("o retangulo é valido!!")
    valor_x = x2 - x1
    valor_y = y2 - y1
    print(valor_x)
    print(valor_y)
    area = (2*valor_x) * (2*valor_y)
    print("A area é: {} m2".format(area))
else:
    print("o retangulo não é valido")