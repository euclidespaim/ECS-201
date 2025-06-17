# Crie um programa em Python que:
# Peça ao usuário um número inteiro.

# Verifique se o número é par ou ímpar usando if.

# Mostre uma mensagem informando o resultado.

num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")
    