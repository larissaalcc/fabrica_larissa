#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
print("-"*127)
c=int(input("Digite a temperatura para ser convertida: "))
f= (c*9/5+32)
print("{}°C convertido são {}°F".format(c,f))