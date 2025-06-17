# Crie um programa em Python que:
# Peça ao usuário a temperatura atual (em graus Celsius).

# Verifique a condição e imprima:

# Se for maior ou igual a 30: "Está quente!"
# Se for menor que 15: "Está frio!"
# Caso contrário: "O clima está agradável."

temp = int(input("Qual é a temperatura atual (em graus Celsius)? "))  

if temp >= 30:
    print("Está quente!")
elif temp < 15:
    print("Está frio!")
else:
    print("O clima está agradável.")