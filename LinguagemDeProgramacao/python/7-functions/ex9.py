# Crie uma função "conta_a()" que:
# Peça uma palavra ao usuário
# Conte quantas letras “a” ela possui, verificando letra por letra

def conta_a():
  palavra = input("Digite uma palavra: ")
  contador = 0
  
  for x in palavra:
    if x == "a":
      contador += 1

  print("A palavra ", palavra, "possui", contador,  " letras 'a'.")
    
# Chame a função
conta_a()