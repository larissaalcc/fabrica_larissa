#2.Crie uma lista com com 10 números e exiba a soma dos números no terminal utilizando a estrutura de repetição FOR.

listan= []
soma=0
for i in range(10):
    listan.append (int(input("\nDigite 1 números: ")))
    
for item in listan:
    soma=soma+item
    
print("A soma dos números listados é igual a: ",soma)