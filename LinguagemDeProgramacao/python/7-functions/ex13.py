# Escreva uma função que:

# Peça ao usuário para digitar 7 números inteiros (um por vez).
# Guarde esses números em uma lista.
# Percorra a lista e conte quantos números são pares e quantos são 
# ímpares.

# Ao final, exiba na tela:
# A lista completa de números digitados.
# A quantidade de números pares.
# A quantidade de números ímpares.

def contar_pares_impares():
    numeros = []
    pares = 0
    impares = 0
    
    for i in range(7):
      num = int(input("Digite um número inteiro: "))
      numeros.append(num)
      
      if num % 2 == 0:
          pares = pares + 1
      else:
          impares += 1
          
    print("Números digitados:", numeros)
    print("Quantidade de números pares:", pares)
    print("Quantidade de números ímpares:", impares)
    
# Chamada da função
contar_pares_impares()
