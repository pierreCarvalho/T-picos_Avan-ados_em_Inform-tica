
#Ler  duas  palavras  e  compará-las.  O  programa  deve  informar  se  as  palavras  são  iguais,  em caso
#contrário,  informar  se  a  primeira  é  maior  do  que a  segunda,  se  a  segunda  é  maior  do  que  a 
#primeira ou se são diferentes e tem o mesmo tamanho.


palavra1 = input("Digite uma palavra qualquer: ")
palavra2 = input("Digite uma palavra qualquer outra vez: ")


if palavra1 == palavra2:
    print("São iguais!")
else:
    print("Não são iguais não") 
    if len(palavra1) > len(palavra2):
        print("A palavra {} é maior que a palavra {}".format(palavra1,palavra2))
    elif len(palavra1) < len(palavra2):
        print("A palavra {} é menor que a palavra {}".format(palavra1,palavra2))
    else:
        print("Tem o mesmo tamanho")