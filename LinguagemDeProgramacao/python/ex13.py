# Crie um programa em Python que:

# Peça a idade da pessoa.
# Informe se ela paga entrada ou tem entrada gratuita:

# Menores de 12 anos e maiores de 60 têm entrada gratuita.

# Todos os demais pagam entrada.

idade = int(input("Digite a sua idade: "))

if idade < 12 or idade > 60:
    print("Entrada gratuita.")
else:
    print("Você precisa pagar a entrada.")
    
    