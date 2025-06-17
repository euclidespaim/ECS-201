# Calculadora com match e if
# O programa deve pedir ao usuário:

# Uma operação (+, -, * ou /)
# Dois números (podem ser decimais)

# Use a estrutura match para identificar a operação escolhida.

# Para o caso da divisão (/), 
# use um if dentro do case para verificar 
# se o segundo número é diferente de zero.

# Se for zero, exiba uma mensagem de erro.
# Caso contrário, realize a divisão normalmente.

# Se a operação digitada for inválida, exiba uma mensagem apropriada.

opercao = input("Digite a operação (+, -, *, /): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

match opercao:
    case '+':
        resultado = num1 + num2
    case '-':
        resultado = num1 - num2
    case '*':
        resultado = num1 * num2
    case '/':
        if num1 and num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero não é permitida."
    case _:
        resultado = "Operação inválida."      