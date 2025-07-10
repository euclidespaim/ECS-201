# Crie uma função quadrado que:
# Receba um número como parâmetro
# Retorne o quadrado desse número

def quadrado(numero):
    return numero ** 2
  

num = int(input("Digite um número: "))
print("O quadrado de", num, "é", quadrado(num), ".")