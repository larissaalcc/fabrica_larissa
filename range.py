'''for a in range(1,11):
    for b in range(1,11):
        print(a,"x",b,"=",a*b)'''

'''for a in range(0,102,2):
    print(a)'''

'''print("-"*197)
soma=0
a= int (input("Número inicial: "))
b= int (input("Número final: "))
for c in range(a,b):
    print(c)
    soma=soma+c
print("A soma dos intervalos é igual a ",soma )
    
for a in range (1,21):
    print(a)
print("-"*178)
for b in range (1,21):
    print(b, end = (","))

v=5 
soma= 0
for a in range (v):
    print("informe o ", a+1)
    num=int(input("Escreva o número: "))
    soma= soma+num
media= soma/5
print( "A soma dos números é: ",soma )
print("A média dos número é igual a: ",media)'''


print("Se quiser sair aperte 'x' ")
lista=[]
while True:
    a= input("Digite o valor: ")
    if a== "x":
        break
    a= int(a)
    lista.append(a)

    
   