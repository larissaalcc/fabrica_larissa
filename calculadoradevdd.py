
while True:
    def calculadora ():
       print("-"*20)
    funcao= (input("Função: \n>> "))
    nloop= float(input("Digite o número: \n>>"))
    if funcao == "+":
     nfinal = nfinal + nloop
     historico = historico + nloop
    elif funcao == "-" :
       nfinal = nfinal - nloop
       historico = historico + nloop
    elif funcao == "/":
       nfinal= nfinal / nloop
       historico = historico + nloop
    elif funcao == "*": 
       nfinal = nfinal * nloop
       historico = historico + nloop
    elif funcao == "=" :
       print(historico)
       print("O resultado do cálculo: \n>>", nfinal)
    def dnv():
       denovo = input("Deseja calcular denovo? \n|I S = sim\n\I N = não\n>> ")
       denovo = denovo.upper
       if denovo == "s":
          calculadora()
       elif denovo == "n":
          print("Saindo...")
          print ("Obrigado por usar nossa calculadora")
       else:
          print("Resposta errada>:")
          dnv()
    calculadora()

   




    