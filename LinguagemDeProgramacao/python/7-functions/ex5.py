# Crie uma função chamada tabuada que:
# Receba um número
# Use um laço for para imprimir sua tabuada de 1 a 10

def tabuda(num):
  for i in range(1, 11):
    print(i, "x", num, "=", i * num)
    
tabuda(3)