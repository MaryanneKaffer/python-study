tamanhos = ("P", "M", "G") # Tamanhos
precosBA = (16.00, 18.00, 22.00) # Preços Bife Acebolado
precosFF = (15.00, 17.0, 21.00) # Preços Filé de Frango

valorTotal = 0 # Valor total da compra e acumulador

print("-" * 10 + "* Bem-Vindo a marmiteria da Maryanne Kaffer! *" + "-" * 10)

# Imprimindo o menu
print("-" * 27 + "* Cardápio *" + "-" * 27)
print("-" * 66)
print(6 * "-" + "| Tamanhos | Bife Acebolado(BA) | Filé de Frango(FF) |" + 6 * "-")
for i in range(len(tamanhos)):
    print(6 * "-" + f"|     {tamanhos[i]}    |       R$ {precosBA[i]}      |      R$ {precosFF[i]}       |" + 6 * "-")
print("-" * 66)

# While para o usuário fazer o pedido
while True:
    # Recebendo o sabor e o tamanho do pedido
    sabor = input("Entre com o sabor desejado (BA/FF): ")
    if sabor != "BA" and sabor != "FF":
        print("Sabor inválido. Tente novamente")
        print()
        continue
    
    tamanho = input("Entre com o tamanho desejado (P/M/G): ")
    if tamanho not in tamanhos:
        print("Tamanho inválido. Tente novamente")
        print()
        continue
    
    # Calculando o valor do pedido
    if sabor == "BA":
        if tamanho == "P":
            valor = 16.00
        elif tamanho == "M":
            valor = 18.00
        else:
            valor = 22.00
        print(f"Você escolheu uma marmita de Bife Acebolado no tamanho {tamanho}: R$ {valor:.2f}")
    else:
        if tamanho == "P":
            valor = 15.00
        elif tamanho == "M":
            valor = 17.00
        else:
            valor = 21.00
        print(f"Você escolheu uma marmita de Filé de Frango no tamanho {tamanho}: R$ {valor:.2f}")
        
    # Acumulando valor total
    valorTotal += valor
    
    print()
    # Verificando se o usuário quer mais alguma coisa
    if input("Deseja mais alguma coisa? (S/N): ") == "S":
        print()
        continue
    else: 
        break
    
# Imprimindo o valor total
print() 
print(f"Total a ser pago: R$ {valorTotal:.2f}")