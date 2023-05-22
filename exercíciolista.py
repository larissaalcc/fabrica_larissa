#recebe e armazena uma lista, depois imprime dados:nome, sobrenome, endereço, bairro, cidade, estado, pais, fone, cpf, 
#peso, altura, idade, cartão, email, cep, n1, n2, n3, n4, média, série, classe, sexo, cor, matrícula
listanome= []
listasobrenome= []
listaendereco= []
listabairro= []
listacidade= []
listaestado= []
listapais= []
listafone= []
listacpf= []
listapeso= []
listaaltura= []
listaidade= []
listacartao=[]
listaemail= []
listacep= []
listan1= []
listan2= []
listan3= []
listan4= []
listamedia= []
listaserie= []
listaclasse=[]
listasexo= []
listacor= []
listamatricula= []


cont= 0
while True:
    p= input("Digite 1 para cadastro, 2 para consulta ou 0 para sair:")
    if p == "0":
        break
    elif p== "1":
        print("Bem vindo, por favor preencha os dados a seguir!")
        nome= input("Digite seu nome: \n")
        listanome.append (nome)

        sobrenome= input("Sobrenome: \n")
        listasobrenome.append(sobrenome)    

        endereco= input("Seu endereço (rua, n°); \n")
        listaendereco.append(endereco)

        bairro= input("Bairro: \n")
        listabairro.append(bairro)

        cidade= input("Cidade: \n")
        listacidade.append(cidade)

        estado= input("Estado: \n")
        listaestado.append(estado)

        pais= input("País: \n")
        listapais.append(pais)
        
        fone= int (input("Telefone para contato: \n"))
        listafone.append(fone)

        cpf= float (input ("CPF: "))
        listacpf.append(cpf)

        peso= float (input("Peso: \n"))
        listapeso.append(peso)

        altura= float (input("Altura: \n"))
        listaaltura.append(altura)

        idade= int (input("Idade: \n"))
        listaidade.append(idade)
       
        cartao= float (input("Número do cartão: \n"))
        listacartao.append(cartao)

        email= input("Email para contato: \n")
        listaemail.append(email)

        cep= float(input("CEP da residência: \n"))
        listacep.append(cep)

        n1= float(input("Primeira nota: "))
        listan1.append(n1)
        n2= float(input("Segunda nota: "))
        listan1.append(n2)
        n3= float(input("Terceira nota: "))
        listan1.append(n3)
        n4= float (input("Quarta nota: "))
        listan1.append(n4)
         
        media= input("Sua média")
        listamedia.append(media)
        
        serie= input("Série: ")
        listaserie.append(serie)

        classe= str(input("Classe: "))
        listaclasse.append(classe)

        sexo= input("Sexo (F para feminino, M para masculino): ")
        listasexo.append(sexo)

        cor= input("Sua cor: ")
        listacor.append(cor)

        cont=cont+1
        listamatricula.append(cont)
    if p=="2":
        print("Vamos consultar sua matrícula!")
        mat= input("Digite o número da sua matrícula:")
        media= (n1+n2+n3+n4)/4
        if mat=="1":
            print(listanome)
            print(listasobrenome)
            print(listaendereco)
            print(listabairro)
            print(listacidade)
            print(listaestado)
            print(listapais)
            print(listafone)
            print(listacpf)
            print(listapeso)
            print(listaaltura)
            print(listacidade)
            print(listacartao)
            print(listaemail)
            print(listacep)
            print(listan1)
            print(listan2)
            print(listan3)
            print(listan4)
            print(media)
            print(listaserie)
            print(listaclasse)
            print(listasexo)
            print(listacor)
        












































































