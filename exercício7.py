s= float(input("Digite seu salário atual: "))
if s<500:
    print('15% de reajuste')
    aumento= (s*15/100)+s
    print (aumento)
elif s>=500:
    print('10% de reajuste')
    aumento= (s*10/100)+s
    print (aumento)
else:
    print('5% de reajuste')
    aumento= (s*5/100)+s
    print (aumento)