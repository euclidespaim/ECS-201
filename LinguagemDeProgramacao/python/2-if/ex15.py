# Peça ao usuário um número inteiro.
# Verifique e informe:

# Se o número é divisível por 3 e por 5 ao mesmo tempo, 
# exiba: "Divisível por 3 e 5!"

# Se for apenas divisível por 3, exiba: "Divisível por 3."
# Se for apenas divisível por 5, exiba: "Divisível por 5."
# Caso contrário, exiba: "Não é divisível por 3 nem por 5."

numero = int(input("Digite um número inteiro: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("Divisível por 3 e 5!")
elif numero % 3 == 0:
    print("Divisível por 3.")
elif numero % 5 == 0:
    print("Divisível por 5.")
else:
    print("Não é divisível por 3 nem por 5.")
# Fim do código