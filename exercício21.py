menor=9999999
maior=-1
for item in range(1,6):
    print("\n")
    codigo=int(input("Digite o código da cidade:"))
    veiculo=int(input("Número de veículos de passeio: "))
    acidente=int(input("Número de acidentes de trânsito com vitimas: "))
    if acidente<menor:
        menor=acidente