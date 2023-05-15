n1= int(input('Primeira nota: '))
n2= int(input('Segunda nota: '))
media= (n1+n2)/2
print(media)
if media>=7:
    print("PARABÉNS, VOCÊ FOI APROVADO!")
elif media >=5:
    print("VOCÊ ESTÁ DE RECUPERAÇÃO!")
else:
    print('LAMENTO, VOCÊ ESTÁ REPROVADO!')