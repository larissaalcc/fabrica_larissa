#Exercício 009
#Faça um Programa que peça a temperatura em graus Farenheit,
#transforme e mostre a temperatura em graus Celsius.
#C = (5 * (F-32) / 9).
print("-"*127)
f= int(input("Indique a tempertura para ser convertida: "))
c= (5*(f-32)/9)
print("{} °F convertido são {}°C".format(f,c))