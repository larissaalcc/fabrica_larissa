lista_mae= []
lista_filho= []
lista_pergunta= ['Nome: ', 'Sobrenome: ', 'Endereço: ','Bairro: ','Cidade: ','Estado: ','País: ','Cpf: ', 'Fone: ', 'Cep: ', 
'Peso: ', 'Altura: ', 'Idade: ','Cartão: ','Email: ', 'Cep: ', 'Nota 1: ', 'Nota 2: ', 'Nota 3: ', 'Nota 4: ', 'Série: ', 'Classe: ', 'Sexo: ','Cor: ',
'Matrícula: ']
while True:
    escolha= int(input(" 1.Cadastrar\n 2.Consultar\n 0.Sair\n escolha: "))
    if escolha== 0:
        break
    elif escolha== 1:
        for c in range (25):
            print(15*"-")
            lista_filho.append(input(f"{lista_pergunta [c]}"))
        print("Cadastrado com sucesso!")

        n1= int(lista_filho[16])
        n2= int(lista_filho[17])
        n3= int(lista_filho[18])
        n4= int(lista_filho[19])
        media= (n1+n2+n3+n4)/4
        lista_filho.append(media)
        lista_mae.append(lista_filho.copy())
        lista_filho.clear()
        
        
    elif escolha == 2:
        matricula= input("Digite o número da matrícula: ")
        for elemento in lista_mae:
         if matricula==elemento[-2]:
            print(f"Número da matrícula {elemento[-2]}\nNome: {elemento[0]} \nSobrenome: {elemento[1]}  \nEndereço: {elemento[2]}  \nBairro: {elemento[3]} \nCidade: {elemento[4]} \nEstado: {elemento[5]} \nPaís: {elemento[6]} \nCPF: {elemento[7]} \nFone: {elemento[8]} \nCEP: {elemento[9]}  \nPeso: {elemento[10]} \nAltura: {elemento[11]} \nIdade: {elemento[12]} \nCartão: {elemento[13]} \nEmail: {elemento[14]}  \nCep: {elemento[15]} \nN1: {elemento[16]} \nN2: {elemento[17]} \nN3: {elemento[18]} \nN4: {elemento[19]} \nmédia: {media} \nSérie: {elemento[20]} \nClasse: {elemento[21]} \nSexo: {elemento[22]} \nCor: {elemento[23]}")
                  

                 
                 



  