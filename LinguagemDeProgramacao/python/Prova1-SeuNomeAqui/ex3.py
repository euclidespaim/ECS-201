# Crie uma função chamada soma_pares_intervalo() que:
# 
# Peça dois números ao usuário, um início e um fim do intervalo
# Some todos os números pares do existentes entre o início e o fim
# Retorne essa soma

def soma_pares_intervalo():
    inicio = int(input("Digite o início do intervalo: "))
    fim = int(input("Digite o fim do intervalo: "))
    
    
    soma = 0
    for num in range(inicio, fim + 1):
        if num % 2 == 0:
            soma += num
            
    return soma
  
# Chamada da função e exibição do resultado
resultado = soma_pares_intervalo()
print("A soma dos números pares no intervalo é:", resultado)