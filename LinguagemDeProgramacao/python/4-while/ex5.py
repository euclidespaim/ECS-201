# Adivinhe o número

# O computador escolhe um número aleatório 
# entre 1 e 10. Peça ao usuário que tente 
# adivinhar o número.

# Enquanto ele errar, mostre: 
# "Errou! Tente novamente."

# Quando acertar, mostre: 
# "Parabéns! Você acertou."
import random
numero_secreto = random.randint(1, 10)

numero = int(input("Tente adivinhar o número entre 1 e 10: "))

while numero != numero_secreto:
    print("Errou! Tente novamente.")
    numero = int(input("Tente adivinhar o número entre 1 e 10: "))
else:
    print("Parabéns! Você acertou.")
    print(f"O número era {numero_secreto}.")
