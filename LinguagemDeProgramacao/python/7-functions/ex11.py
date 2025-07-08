# Crie uma função conta_negativos que:

# Peça ao usuário 3 números
# Conte quantos são negativos


def conta_negativos():
    contador = 0
    
    for i in range(3):
        num = int(input("Digite um número: "))
        
        if num < 0:
            contador += 1
    
    print("Você digitou", contador, "números negativos.")
    
# Chame a função
conta_negativos()