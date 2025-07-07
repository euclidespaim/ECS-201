# Crie uma função chamada verifica_par que receba um 
# número como parâmetro e diga se ele é par ou ímpar 
# usando if.

def verifica_par(num):
  if num % 2 == 0:
    print("O número é par!")
  else:
    print("O número é impar!!")
    
verifica_par(int(input("Digite um número: ")))