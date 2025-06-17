# Crie um programa que simule um sistema de login simples. 
# Peça ao usuário que digite uma senha. 
# Se a senha for igual a "elfrida2025", exiba a 
# mensagem "Acesso permitido". 
# Caso contrário, exiba "Senha incorreta. Tente novamente."


usuario = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

if senha == "elfrida2025":
  print("Acesso permitido" , usuario, "!" )
else:
  print("Senha incorreta. Tente novamente.")
  print("Acesso negado!")
  
  