# Cálculo da Média de Notas
# Solicite ao usuário as notas de 2 disciplinas e 
# calcule a média. Se a média for maior ou igual a 7, 
# informe "Aprovado". Caso contrário, informe "Reprovado".


nota1 = float(input("Digite a nota da primeira disciplina: "))
nota2 = float(input("Digite a nota da segunda disciplina: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
    print("Parabéns!!")
    
if media < 7:
    print("Reprovado")
    print("Estude mais!!")