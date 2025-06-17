# Nível 1 – Criação e Manipulação
# Crie uma lista chamada cores com os valores 
# "vermelho", "azul" e "verde".

# 1.Mostre na tela o primeiro item da lista cores.
# 2.Troque o valor "azul" por "amarelo" na lista.
# 3.Adicione "preto" ao final da lista usando append().
# 4.Insira "branco" na segunda posição usando insert().
# 5.Remova a cor "verde" da lista usando remove().
# 6.Remova o último item usando pop() sem passar índice.
# 7.Remova o item da posição 0 usando pop() com índice.
# 8.Mostre quantos itens existem na lista usando len().

cores = ["vermelho", "azul", "verde"]
print(cores[0])  # Mostra o primeiro item da lista
cores[1] = "amarelo"  # Troca "azul" por "amarelo"
cores.append("preto")  # Adiciona "preto" ao final da lista
cores.insert(1, "branco")  # Insere "branco" na segunda posição
cores.remove("verde")  # Remove "verde" da lista
cores.pop()  # Remove o último item da lista
cores.pop(0)  # Remove o item da posição 0
print(len(cores))  # Mostra quantos itens existem na lista