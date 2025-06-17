# Crie um programa em Python que peça ao usuário 
# para escolher uma opção de verificação numérica.

# O programa deve mostrar o seguinte menu:

# Escolha uma opção:
# 1 - Verificar se um número é par ou ímpar
# 2 - Verificar se um número é positivo, negativo ou zero
# 3 - Sair

# Use a estrutura match para tratar cada opção.
# Dentro do case 1, use if para verificar se o número é par ou ímpar.
# Dentro do case 2, use if para verificar se o número é positivo, negativo ou zero.
# Se a opção for 3, exiba a mensagem "Saindo do programa...".
# Para qualquer outro valor, exiba "Opção inválida."

opcao = input("Escolha uma opção:\n1 - Verificar se um número é par ou ímpar\n2 - Verificar se um número é positivo, negativo ou zero\n3 - Sair\n")

match opcao:
    case "1":
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print("O número é par.")
        else:
            print("O número é ímpar.")
    case "2":
        numero = int(input("Digite um número: "))
        if numero > 0:
            print("O número é positivo.")
        elif numero < 0:
            print("O número é negativo.")
        else:
            print("O número é zero.")
    case "3":
        print("Saindo do programa...")
    case _:
        print("Opção inválida.")