# Implemente um programa que solicite a senha 
# de acesso ao usuário. O laço while deve 
# continuar pedindo a senha até que o usuário 
# acerte. A senha correta é "python123".
# Extra: Mostre uma mensagem de sucesso ao final.

senha_correta = "python123"
senha = input("Digite a senha: ")

while senha != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")
else:
    print("Senha correta! Acesso concedido.")
