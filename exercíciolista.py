#recebe e armazena uma lista, depois imprime dados:nome, sobrenome, endereço, bairro, cidade, estado, pais, fone, cpf, 
#peso, altura, idade, cartão, email, cep, n1, n2, n3, n4, média, série, classe, sexo, cor, matrícula
lnome= []
lsobrenome= []
lendereco= []
lbairro= []
lcidade= []
lestado= []
lpais= []
lfone= []
lcpf= []
lpeso= []
laltura= []
lidade= []
lcartao=[]
lemail= []
lcep= []
ln1= []
ln2= []
ln3= []
ln4= []
lmedia= []
lserie= []
lclasse=[]
lsexo= []
lcor= []
lmatricula=[]

cont= 0
while True:
    p= input("Digite 1 para cadastro, 2 para consulta ou 0 para sair:")
    if p == "0":
        break
    elif p== "1":
        cont=cont+1
        mat=cont
        print("Bem vindo, por favor preencha os dados a seguir!")
        nome= str (input("Digite seu nome: "))
        lnome.append (nome)

        sobrenome= str(input("Sobrenome: "))
        lsobrenome.append(sobrenome)    

        endereco= str (input("Seu endereço (rua, n°); "))
        lendereco.append(endereco)

        bairro= str (input("Bairro: "))
        lbairro.append(bairro)

        cidade= str (input("Cidade: "))
        lcidade.append(cidade)

        estado= str (input("Estado: "))
        lestado.append(estado)

        pais= str (input("País: "))
        lpais.append(pais)
        
        fone= int (input("Telefone para contato: "))
        lfone.append(fone)

        cpf= int (input ("CPF: "))
        lcpf.append(cpf)

        peso= int (input("Peso: "))
        lpeso.append(peso)

        altura= float (input("Altura: "))
        laltura.append(altura)

        idade= int (input("Idade: "))
        lidade.append(idade)
       
        cartao= float (input("Número do cartão: "))
        lcartao.append(cartao)

        email= str (input("Email para contato: "))
        lemail.append(email)

        cep= int(input("CEP da residência: "))
        lcep.append(cep)

        n1= int(input("Primeira nota: "))
        ln1.append(n1)
        n2= int(input("Segunda nota: "))
        ln2.append(n2)
        n3= int(input("Terceira nota: "))
        ln3.append(n3)
        n4= int (input("Quarta nota: "))
        ln4.append(n4)
         
        media= print("Sua média: ")
        media= (n1+n2+n3+n3)/4
        print(media)   
        lmedia.append(media)
        
       
        
        serie= int (input("Série: "))
        lserie.append(serie)

        classe= str(input("Classe: "))
        lclasse.append(classe)

        sexo= str (input("Sexo (F para feminino, M para masculino, O para outros): "))
        lsexo.append(sexo)
        if sexo== "f" or sexo== "F":
            print("feminino")
        elif sexo =="m" or sexo == "M":
            print("masculino")
        elif sexo == "o" or sexo== "O":
            print("outro")
        else:
            print("sexo não definido")
        cor= input("Sua cor: ")
        lcor.append(cor)
        print(">>>>CADASTRO CONCLUÍDO<<<< \n")
    elif p=="2":

        print("Vamos consultar sua matrícula!\n")
        mat= input("Digite o número da sua matrícula:\n")
        
        print("MATRÍCULA",cont[mat-1], "\nNOME:", lnome[mat-1], "\nSOBRENOME:",lsobrenome[mat-1],"ENDEREÇO:", lendereco[mat-1], "BAIRRO:",lbairro[mat-1], "CIDADE:", lcidade[mat-1],"ESTADO:",lestado[mat-1], "PAÍS:",lpais[mat-1],"FONE:", lfone[mat-1],  "CPF:", lfone[mat-Exception has occurred: TypeError
             unsupported operand type(s) for -: 'str' and 'int'
               File "C:\Users\IANGA\Documents\GitHub\fabrica_larissa\exercíciolista.py", line 123, in <module>
                 print("MATRÍCULA",cont[mat-1], "\nNOME:", lnome[mat-1], "\nSOBRENOME:",lsobrenome[mat-1],"ENDEREÇO:", lendereco[mat-1], "BAIRRO:",lbairro[mat-1], "CIDADE:", lcidade[mat-1],
                                        ~~~^~
             TypeError: unsupported operand type(s) for -: 'str' and 'int'1], "PESO:", lpeso[mat-1],"ALTURA:", laltura[mat-1], lcartao [mat-1], "EMAIL:", lemail[mat-1],"CEP:",lcep[mat-1],"N1:" ,ln1[mat-1],"N2:", ln2[mat-1],"N4:",ln3[mat-1],"MÉDIA:",lmedia[mat-1], "SÉRIE:", lserie[mat-1],
             "CLASSE:", lclasse [mat-1],"SEXO:",lsexo[mat-1],"COR",lcor[mat-1] )
      
        
        












































































