# Receba o nome de uma fruta e a quantidade desejada.
# Se for "maçã" e a quantidade for maior que 5, aplique desconto.

fruta = input("Digite o nome da fruta: ").lower()
quantidade = int(input("Digite a quantidade desejada: "))

match fruta:
    case "maçã":
        if quantidade > 5:
            print("Desconto aplicado para: ", fruta)
        else:
            print("Sem desconto para: ", fruta)
    case _:
        print("Fruta não disponível.")
# Fim do código