# Operações básicas com dois números

# Faça um programa que leia dois números reais e mostre o
# resultado da soma, subtração, multiplicação e divisão entre eles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
multiplicacao = num1 * num2
subtracao = num1 - num2
divisao = num1 / num2

print("Soma: ", soma)
print("Multiplicação: ", multiplicacao)
print(f"Subtração: {subtracao}")
print(f"Divisão: {divisao}")