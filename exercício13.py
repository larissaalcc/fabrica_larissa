a=int(input("Digite o numero A: "))
b=int(input("Digite o numero B: "))
c=int(input("Digite o numero C: "))

if a>=b and a>=c and b>=c :
    print(f"A ordem decresente é {a},{b},{c}")

elif a>=b and a>=c and c>=b :
    print(f"A ordem decresente é {a},{c},{b}")
elif b>=a and b>=c and a>=c :
    print(f"A ordem decresente é {b},{a},{c}")
elif b>=a and b>=c and c>=a :
    print(f"A ordem decresente é {b},{c},{a}")
elif c>=a and c>=b and a>=b :
    print(f"A ordem decresente é {c},{a},{b}")
elif c>=a and c>=b and b>=a :
    print(f"A ordem decresente é {c},{b},{a}")