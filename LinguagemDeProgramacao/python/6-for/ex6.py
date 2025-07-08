# Escreva um programa que peça um número ao usuário 
# e exiba sua tabuada de multiplicação de 1 a 10.

numero = int(input("Digite um númeor inteiro: "))


for multi in range(1, 11):
    print(f"{numero} x {multi} = {numero * multi}")