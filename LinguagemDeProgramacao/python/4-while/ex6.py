# Peça ao usuário para digitar um número 
# inteiro positivo.
# O programa deve fazer uma contagem 
# regressiva a partir desse número até 0, 
# mostrando um número por segundo.
# Ao final, exiba a mensagem "BUM!".

import time
tempo = int(input("Digite um número inteiro positivo: "))

while tempo >= 0:
  print(tempo)
  time.sleep(1)  # Pausa de 1 segundo
  tempo -= 1
  tempo = tempo -1
else:
  print("BUM! 💥")

