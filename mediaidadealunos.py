import os 
print("Cadastro da idade dos alunos\n")
cont=0
soma=0
alunos= int(input("Informe a quantidade de alunos matriculados: "))
while cont<alunos:
    cont=cont+1
    idade=int(input("Digite a idade do aluno: "))
    soma=soma+idade
    media=soma/alunos 
print ("A sala tem {} alunos e a média de idade é {}".format(alunos,media))
if media >0 and media<=25:
    print("A turma é jovem!")
elif media >25 and media <60:
    print("Aturma é adulta!")
else:
    print("A turma é idosa")
os.system('pause')
