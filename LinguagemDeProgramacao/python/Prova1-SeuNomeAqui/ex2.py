# crie uma funcao conta_50 que peça ao usuário 7 números conte quantos 
# desses números são menores que 50 e mostre o resultado na tela

def conta_50():
    contador = 0

    for i in range(7):
      num = int(input("Digite um número:"))

      if num < 50:
       contador = contador + 1 

    print("Você digitou", contador, "números menores que 50.")


conta_50()