print("Bem-Vindo à Loja da Maryanne Kaffer")

# Recebendo os valores do pedido e a quantidade de parcelas
valorDoPedido = float(input("Entre com o valor do pedido: "))
quantidadeParcelas = int(input("Entre com a quantidade de parcelas: "))

# Definindo o valor dos juros de acordo com a quantidade de parcelas
if quantidadeParcelas < 4:
    juros = 0
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 0.04
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 0.08
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 0.16
else:
    juros = 0.32

# Calculando o valor da parcela e o valor total parcelado
valorDaParcela = valorDoPedido * (1 + juros) / quantidadeParcelas
valorParcelado = valorDaParcela * quantidadeParcelas

# Imprimindo os valores
print("O valor das parcelas é de: R${:.2f}".format(valorDaParcela))
print("O valor total parcelado é de: R${:.2f}".format(valorParcelado))