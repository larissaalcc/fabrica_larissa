n1= str(input("Nome do produto 1:"))
p1= float(input('preço 1: '))
n2= str(input("Nome do produto 2:"))
p2= float(input('preço 2: '))
n3= str(input("Nome do produto 3:"))
p3= float(input('preço 3: '))
if p1<p2 and p1<p3:
    print ("O produto %s é mais barato e custa R$%s"%(n1,p2))
if p2<p1 and p2<p3:
    print ("O produto %s é mais barato e custa R$%s" %(n2,p2))
if p3<p1 and p3<p2:
    print ("O produto %s é mais barato e custa R$%s"% (n3,p3))
