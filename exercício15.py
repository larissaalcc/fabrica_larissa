#laço infinito

'''while True: 
   print ("Laço infinito \n")'''

#contar oba de 1 ao 10
'''a=1 
while a >=0 and a<= 10: 
    a += 1 
    print ("OBA")'''

while True: #sempre verdadeiro
    valor= int(input("Digite o valor 1 ou 0 para encerrar \n"))
    if valor == 1: 
        print ('Valor correto')
    else:
        print ('Valor para sair')
        break
    