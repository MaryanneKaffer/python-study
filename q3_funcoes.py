modelos = ("Manga Curta Simples - MCS", "Manga Longa Simples - MLS", "Manga Curta Com Estampa - MCE", "Manga Longa Com Estampa - MLE")
fretes = ("1 - Frete por transportadora - R$ 100.00", "2 - Frete por Sedex - R$ 200.00", "0 - Retirar na fábrica - R$ 0.00")

def escolha_modelo():
    # Recebendo o modelo desejado
    while True:
        print("Escolha o modelo desejado:")
        for i in range(len(modelos)):
            print(modelos[i])
        pedido = input("Modelo: ")
        # Decidindo o valor unitário de acordo com o modelo
        if pedido == "MCS":
            valorUn = 1.80
        elif pedido == "MLS":
            valorUn = 2.10
        elif pedido == "MCE":
            valorUn = 2.90
        elif pedido == "MLE":
            valorUn = 3.20
        else: # Validação
            print("Modelo inválido. Tente novamente")
            print()
            continue
        print()
        return valorUn
    
def num_camisetas():
    # Recebendo a quantidade de camisetas do pedido
    while True:
        try:
            quantidade = int(input("Informe a quantidade: "))
            if quantidade < 1 or quantidade > 20000: # Validação
                print("Quantidade inválida. Tente novamente")
                print()
                continue
        except ValueError:
            print("Quantidade inválida. Tente novamente")
            print()
            continue
        # Calculando o desconto de acordo com a quantidade
        if quantidade >= 20 and quantidade < 200:
            desconto = 0.05
        elif quantidade >= 200 and quantidade < 2000:
            desconto = 0.07
        elif quantidade >= 2000 and quantidade <= 20000:
            desconto = 0.12
        else:
            desconto = 0
        break
    # Retornando a quantidade de camisetas com desconto
    return int(quantidade * (1 - desconto))

def frete():
    print()
    # Recebendo o tipo de frete
    while True:
        try:
            print("Escolha o tipo de frete:")
            for i in range(len(fretes)):
                print(fretes[i])
            frete = int(input("Frete: "))
            if frete > 2 or frete < 0: # Validação
                print("Frete inválido. Tente novamente")
                print()
                continue
            else:
                # Decidindo o valor do frete
                if frete == 1:
                    valorFrete = 100
                elif frete == 2:
                    valorFrete = 200
                else:
                    valorFrete = 0
                break
        except ValueError: # Validação
            print("Frete inválido. Tente novamente")
            print()
            continue
    return valorFrete

# Programa Principal
print("-* Bem-Vindo à Fábrica da Maryanne Kaffer *-")
print()

# Chamando as funções
modeloVal = escolha_modelo()
quantidade = num_camisetas()
valorFrete = frete()

# Calculando o valor total
total = modeloVal * quantidade + valorFrete

# Imprimindo o valor total
print()
print(f"total: R$ {total:.2f} (Modelo: {modeloVal} * Quantidade(Com Desconto): {quantidade} + Frete: {valorFrete:.2f})")