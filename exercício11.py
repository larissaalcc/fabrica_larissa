n1= int(input("Digite um número: "))
n2= int(input("Digite um segundo número: "))
n3= int(input("Digite um terceiro número: "))
if n1>n2 and n2>n3:
    print(n1, n3)
if n2>n1 and n3>n1:
    print(n2, n1)
elif n3>n1 and n2>n1:
    print(n3, n2)