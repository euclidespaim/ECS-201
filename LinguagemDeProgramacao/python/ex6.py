# Média de três números
# Faça um programa que leia três números reais
# e calcule a média aritmética entre eles. 
# Mostre o resultado na tela.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

media = (num1 + num2 + num3) / 3

print("A média aritmética é: ", media)
print(f"A média aritmética é: {media:.2f}")