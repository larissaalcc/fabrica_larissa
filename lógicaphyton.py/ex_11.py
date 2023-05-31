#Exercício 011
#Faça um Programa que peça 2 números inteiros e um número real. 
#Calcule e mostre: o produto do dobro do primeiro com metade do segundo. 
#a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.

print("-"*127)
n1= int(input("Digite um número: "))
n2= int(input("Digite outro número: "))
n3= int(input("Digite outro número: "))
m= (n1*2*n2/2)
s= (n1*3+n3)
p= (n3*n3*n3)
print("O produto do dobro do primeiro número com metade do segundo número é igaul a: {}".format(m))
print("A soma do triplo do primeiro número com o terceiro número é igual a: {}".format(s))
print("O terceiro número elevado ao cubo é igual a: {}".format(p))