// Declare as seguintes variáveis: nome do funcionario, anoNascimento, numero de filhos, rg, 
// salario, ativo. Atribua valores as respectivas variáveis. A variável ativo deverá receber 
// um valor  lógico.  Mostre os dados conforme exemplo abaixo: 

// O funcionário <<nome>>  com rg <<rg>> possui <<>> anos de vida.  O salario do 
// funcionario << nome>> é de R$ << salario>> e possui << >> filhos. Situação ativo:<<ativo>>

programa {
    funcao inicio() {
        // Declaração das variáveis
        cadeia nomeFunc
        inteiro anoNasc, numFilhos, rg, idade
        real salario
        lógico ativo
        
        // Atribuição de valores às variáveis
        nomeFunc = "João Silva"
        anoNasc = 1985
        numFilhos = 3
        rg = "12.345.678-9"
        salario = 3500.00
        ativo = verdadeiro
        
        // Cálculo da idade
        anoAtual = 2025
        idade = anoAtual - anoNasc
        
        // Exibição dos dados
        escreva("O funcionário ", nomeFunc, " com rg ", rg, " possui ", idade, " anos de vida.")
        escreva("\nO salário do funcionário ", nomeFunc, " é de R$ ", salario, " e possui ", numFilhos, " filhos.")
        escreva("\nSituação ativo: ", ativo)
    }
}
