# Crie um programa em Python que:

# Pergunte a idade do usuário.
# Pergunte a classificação indicativa do filme 
# (valores possíveis: L, 10, 12, 14, 16, 18).
# Use estruturas if para verificar se a pessoa pode assistir ao filme.
# Mostre uma das mensagens:
# "Você pode assistir ao filme."
# "Você **não** pode assistir a este filme."

# Entrada de dados
idade = int(input("Qual é a sua idade? "))
classificacao = input("Classificação indicativa do filme (L, 10, 12, 14, 16, 18): ")

# Verifica se a pessoa pode assistir
if classificacao == "L":
    print("Você pode assistir ao filme.")
elif classificacao == "10" and idade >= 10:
    print("Você pode assistir ao filme.")
elif classificacao == "12" and idade >= 12:
    print("Você pode assistir ao filme.")
elif classificacao == "14" and idade >= 14:
    print("Você pode assistir ao filme.")
elif classificacao == "16" and idade >= 16: 
    print("Você pode assistir ao filme.")
elif classificacao == "18" and idade >= 18:
    print("Você pode assistir ao filme.")
else:
    print("Você **não** pode assistir a este filme.")
