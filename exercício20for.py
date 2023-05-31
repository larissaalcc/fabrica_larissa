print(("\n TABELA DE PREÇO - LOJA QUASE DOIS"))
preco=float(input("Valor do pão: "))
for i in range(1,51):
    p=i*preco
    print("{} - R$ {:.2f}".format(i,p))