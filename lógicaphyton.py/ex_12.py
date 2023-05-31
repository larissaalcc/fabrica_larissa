#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas: Para homens: (72,7 h) - 58 Para mulheres: (62,1 h) - 44,7

print("-"*127)
print(">>>>>Vamos calcular o seu peso ideal<<<<<")
s= str(input("Informe seu sexo (M para masculino, F para feminino): "))
h= float(input("Informe sua altura: "))
if s== "f" or "F":
    p= (62.1*h)-(44.7)
    print("Seu peso ideal é {}".format(p))
elif s== "m" or "M":
    p2= (72.7*h)-(58)
    print("Seu peso ideal é: {}".format(p2))