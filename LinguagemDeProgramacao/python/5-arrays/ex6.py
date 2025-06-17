# Crie uma lista chamada idades contendo as idades 
# de 3 pessoas.

# Depois, faça o seguinte:

# Mostre a idade da pessoa mais nova.
# Mostre a idade da pessoa mais velha.

idades = [23, 19, 17]

# Assume que o primeiro item é o maior e o menor 
# inicialmente
maior = idades[0]
menor = idades[0]

if idades[1] > maior:
  maior = idades[1]
if idades[1] < menor:
  menor = idades[1]
  
if idades[2] > maior:
  maior = idades[2]
if idades[2] < menor:
  menor = idades[2]
  
print("a maior idade é: ", maior)
print("a menor idade é: ", menor)