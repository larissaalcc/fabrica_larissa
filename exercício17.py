while True:

 print ("-"*10, "Calculator", "-"*10)


 print(" Digite 1 para Multiplicar: ")
 print(" Digite 2 para Subtrair: ")
 print(" Digite 3 para Adicionar: ")
 print(" Digite 4 para Raiz Quadrada: ")
 print(" Digite 5 para Área de um quadrado: ")
 print(" Digite 6 para Média de 4 números: ")
 print(" Digite 7 para Fatoração: ")
 print(" Digite 8 para Exponenciação: ")
  
 res= int(input())
 if res == 1:
        print("="*10, "Multiplicação", "="*10)
        print("Olá, Bem vindo a multiplicação!")
        b= float(input("Digite um número: "))
        c= float(input("Digite outro número: "))
        a= b*c
        print(" O resultado dessa operação é: ",a)
        print("----FIM----")
 elif  res == 2:
        print("="*10, "subtração", "="*10)
        print("Olá, Bem vindo a subtração!")
        b= float(input("Digite um número: "))
        c= float(input("Digite outro número: "))
        a= b-c
        print(" O resultado dessa operação é: ",a)
        print(    "----FIM----")
 elif  res == 3:
        print("="*10, "adição", "="*10)
        print("Olá, Bem vindo a adição!")
        b= float(input("Digite um número: "))
        c= float(input("Digite outro número: "))
        a= b+c
        print(" O resultado dessa operação é: ",a)
        print("----FIM----")
 elif  res == 4:
        print("="*10, "Raiz quadrada", "="*10)
        print("Olá, Bem vindo a Raiz quadrada!")
        b= float(input("Digite um número: "))
        a= b/b
        print(" O resultado dessa operação é: ",a)
        print("----FIM----")
 elif  res == 5:
        print("="*10, "Área de um quadrado", "="*10)
        print("Olá, Bem vindo a área de um quadrado")
        b= float(input("Digite o lado: "))
        a= b*b
        print(" O resultado dessa operação é: ",a)
        print("----FIM----")
 elif  res == 6:
        print("="*10, "Média", "="*10)
        print("Olá, Bem vindo a média!")
        b= float(input("Primeira nota: "))
        c= float(input("Segunda nota: "))
        d= float(input("Terceira nota "))
        e= float(input("Quarta nota"))
        media = (b+c+d+e)/4
        print(" O resultado dessa operação é: ",media)
        print("----FIM----")
 elif  res == 7:
        print("="*10, "Fatoração", "="*10)
        print("Olá, Bem vindo a fatoração!")
        b= float(input("Digite um número: "))
        c= float(input("Digite outro número: "))
        a= b*c
        print(" O resultado dessa operação é: ",a)
        print("----FIM----")
 elif  res == 8:
        print("="*10, "Fatoração", "="*10)
        print("Olá, Bem vindo a fatoração!")
        b= float(input("Digite um número: "))
        c= float(input("Digite outro número: "))
        a= b*c
        print(" O resultado dessa operação é: ",a)
        print("----FIM----")
 elif res == 7:
        print ("="*10, "Fatorial", "="*10)
        print ("Olá, bem vindo a Fatorial")
        c = float(input("Digite um numero: "))
        result = 1
        contador = 1
        while contador <= c:

            result *= contador
            contador += 1
        print (result)
 elif res == 8:
        print ("="*10, "Exponenciação", "="*10)
        print ("Olá, bem vindo a Exponenciação")
        c = float(input("Digite um numero: "))
        d = float(input("Digite um numero: "))
        b = c**d
        print ("Bom, o resultado dessa operação é: ",b)
        print ("="*10, "Fim - Exponenciação - Fim", "="*10)
        continue
 elif res == 9:
        print ("="*10, "Volume de um Cubo", "="*10)
        print ("Olá, bem vindo a Volume de um Cubo")
        c = float(input("Digite um numero: "))
        d = float(input("Digite um numero: "))
        b = c**2**1
        print ("Bom, o resultado dessa operação é: ",b)
        print ("="*10, "Fim - Volume de um Cubo - Fim", "="*10)
        continue
 elif res == 10:
        print ("="*10, "Divisão", "="*10)
        print ("Olá, bem vindo a Divisão")
        c = float(input("Digite um numero: "))
        d = float(input("Digite um numero: "))
        b = c/d
        print ("Bom, o resultado dessa operação é: ",b)
        print ("="*10, "Fim - Divisão - Fim", "="*10)
        continue
 else: 
        break

     
     


    