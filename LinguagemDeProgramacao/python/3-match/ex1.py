# Crie um programa que
# Mostre um pequeno menu com três opções:

# 1 - Ver saldo
# 2 - Fazer depósito
# 3 - Sair

# Leia a opção escolhida pelo usuário.

# Use match para mostrar a resposta correspondente.

print("Selecione uma das opções a seguir: ")
opcao = input("1 - Ver saldo\n2 - Fazer depósito\n3 - Sair\nOpção: ")

match opcao:
  case "1":
    print("Opção ver saldo selecionada!")
  case "2":
    print("Opção fazer depósito selecionada!")
  case "3":
    print("Opção sair selecionada!")
  case _:
    print("Opção inválida!!")