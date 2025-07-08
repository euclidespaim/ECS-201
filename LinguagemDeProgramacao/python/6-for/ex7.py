# Faça um programa que imprima uma contagem regressiva 
# de 10 até 1, e ao final exiba "FIM!".

import time

for i in range(10, 0, -1):
  time.sleep(1)
  print(i)
  
print("FIM!")