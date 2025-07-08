# 13. Peça nomes ao usuário até que ele digite "sair". 
# Guarde todos os nomes em uma lista e,
# no final, mostre todos os nomes digitados.

nomes = []
entrada = input("Digite um nome (ou 'sair' para encerrar): ")

while entrada != "sair":
    nomes.append(entrada)
    entrada = input("Digite um nome (ou 'sair' para encerrar): ")

print("Nomes digitados:", nomes)