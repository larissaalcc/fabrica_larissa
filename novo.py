while True:
    n1= int(input("Digite o primeiro número: "))
    escolha= int(input("1. Adição 2.Subtração 3.Divisão 4. Multiplicação 5.reset 6.sair "))
    n2=int(input("Digite o segundo número: "))
    if escolha == 1:
        resultado= n1+n2
        break
    if escolha == 2:
        resultado= n1-n2
        break
    if escolha == 4:
        resultado = n1*n2
        break
    try:
        if escolha == 3:
            resultado= n1/n2
            break
    except:
        print("erro")
        continue
resultado=resultado

while True:
    print(resultado)
    escolha= int(input("1. Adição 2.Subtração 3.Divisão 4. Multiplicação 5.reset 6.sair "))
    if escolha== 6:
        break
    if escolha== 5:
        resultado= n=0
        continue
    n= int(input("Digite um número: "))
    if escolha == 1:
        resultado= resultado+n
    if escolha == 2:
        resultado= resultado-n
    if escolha == 3:
        resultado= resultado/n
    if escolha == 4:
        resultado= resultado*n

    
        




