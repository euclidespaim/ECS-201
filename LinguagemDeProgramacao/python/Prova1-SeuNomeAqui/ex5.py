# Crie uma função chamada diferenca que:
# Receba dois números como parâmetros
# Calcule e retorne a diferença entre o maior e o menor número
# No programa principal:
# Peça dois números ao usuário
# Chame a função e mostre a diferença

def diferenca(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1
    
# Programa principal
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = diferenca(numero1, numero2)
print("A diferença entre os números é:", resultado)
