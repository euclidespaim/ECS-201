# Peça para o usuário digitar números inteiros. 
# O programa deve continuar pedindo números até que 
# o usuário digite 0. 
# Ao final, mostre a soma de todos os números digitados.


numero = int(input("Digite um número inteiro (0 para sair): "))
soma = 0

while numero != 0:
  soma = soma + numero
  numero = int(input("Digite um número inteiro (0 para sair): "))
else:
  print("A soma dos números digitados é: ", soma)

