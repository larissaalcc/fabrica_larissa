#Exercício 008
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.
print("-"*127)
s= float(input("Seu salário por hora: "))
h= float(input("Horas trabalhadas no mês: "))
t= s*h
print("Seu salário referente a esse mês será de: R$ {}".format(t))