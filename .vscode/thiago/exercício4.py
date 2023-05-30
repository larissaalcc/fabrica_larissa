#4.Crie uma lista vazia, que será usado para receber 10 números com a estrutura FOR apresente ao final o total de números negativos e positivos digitados pelo usuário.
lista=[]
contn= 0
contp= 0
for l in range(10):
    pn=(int(input("Digite um número: ")))
    lista.append(pn)

    if pn < 0:
        contn= contn+1
    elif pn > 0:
        contp= contp+1
print("Números Negativos:",contn)
print("Números Positivos:",contp)



