# Crie uma função conta_maiores_10 que:
# Peça ao usuário 5 números
# Conte quantos são maiores que 10 e mostre o resultado

def conta_maiores_10():
  contador = 0
  
  for i in range(5):
    num = int(input("Digite um número: "))
    
    if num > 10:
      contador = contador + 1
  
  print("Você digitou", contador, "números maiores que 10.")
  
  
# Chame a função
conta_maiores_10()