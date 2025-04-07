def main():
  nome = input("Digite o nome do aluno do Elfrida: ")
  nota1 = float(input("Digite a nota 1: "))
  nota2 = float(input("Digite a segunda nota: "))
  nota3 = float(input("Digite a nota três: "))

  media = (nota1 + nota2 + nota3) / 3

  if media >= 6.0:
    print(f"{nome} está aprovado com média {media:.2f}, parabéns!")
  else:
    print(f"{nome} está reprovado com média {media:.2f}, vai estudar!")

if __name__ == "__main__":
  main()
  