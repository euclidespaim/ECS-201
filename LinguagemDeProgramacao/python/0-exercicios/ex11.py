# 12. Crie uma lista com 5 números e faça um programa 
# que calcule a soma de todos eles.

numeros = []
soma = 0

for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)
    soma += num

print("A soma dos números é:", soma)
