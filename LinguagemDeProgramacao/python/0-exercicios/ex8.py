#10. Faça um programa que peça 5 números ao usuário, 
# armazene na lista e depois exiba todos.

numeros = []

for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

print("Números digitados:", numeros)