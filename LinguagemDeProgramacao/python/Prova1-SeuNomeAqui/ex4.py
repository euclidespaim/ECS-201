def repetir_frase(frase, n):
    for i in range(n):
        print(frase)

# Programa principal
texto = input("Digite a frase: ")
vezes = int(input("Digite o número de vezes que deseja repetir: "))

repetir_frase(texto, vezes)

