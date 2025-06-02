# Crie um programa em Python que:

# Peça a idade da pessoa.

# Pergunte se ela sabe ler e escrever (s para sim, n para não).
# Verifique se ela pode tirar a carteira de motorista:

# Tem que ter 18 anos ou mais e saber ler e escrever.

idade = int(input("Digite a sua idade: "))
ler = input("Você sabe ler (digite s -sim ou n - não)")

if idade > 18 and ler == "s":
  print("Vai na fé meu brother!!")
else: 
  print("Não foi dessa vez!!")