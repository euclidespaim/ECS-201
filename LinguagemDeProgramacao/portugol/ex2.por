programa
{
  funcao inicio()
  {
    cadeia nome
    real nota1, nota2, media
    inteiro frequencia

    escreva("Digite o nome do aluno: ")
    leia(nome)

    escreva("Digite a primeira nota: ")
    leia(nota1)

    escreva("Digite a segunda nota: ")
    leia(nota2)

    escreva("Digite a frequência (em %): ")
    leia(frequencia)

    media = (nota1 + nota2) / 2

    se (media > 6 e frequencia > 75)
    {
      escreva("Aluno ", nome, " está aprovado.")
    }
    senao
    {
      escreva("Aluno ", nome, " está reprovado.")
    }
  }
}