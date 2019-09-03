valor = 1000
soma = 0
flag = True
for i in range(1,51):
    print(soma)
    if flag:
        soma =  soma + (valor/i)
        flag = False
    else:
        soma =  soma - (valor/i)
        flag = True
    valor = valor - 3
    
print(soma)