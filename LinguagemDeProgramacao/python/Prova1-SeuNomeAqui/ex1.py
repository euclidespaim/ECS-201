# Crie uma função chamada potencias que:
# Recebe um número inteiro como parâmentro, 
# calcula e retorna o quadrado e o cubo desse
# número.

def potencias(numero):
    quadrado = numero ** 2
    cubo = numero ** 3
    return quadrado, cubo

num = int(input("Digite um número inteiro: "))
print(potencias(num))
