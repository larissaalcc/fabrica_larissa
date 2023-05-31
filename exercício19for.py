print("\n")
lista_c1=0
lista_c2=0
lista_c3=0
cont=0
votos=0
e= int(input("Quantos eleitores votarão? "))
for i in range(e):
    v=input("Escolha seu eleitor:\n 1.A \n 2.B \n 3.C \n Seu voto: ")
    if v =="1":
        lista_c1=lista_c1+1
    elif v== "2":
        lista_c2=lista_c2+1
    elif v== "3":
        lista_c3=lista_c3+1
print("\n O eleitor A recebeu {} votos\n O eleitor B recebeu {} votos\n O eleitor C recebeu {} votos".format(lista_c1,lista_c2,lista_c3))