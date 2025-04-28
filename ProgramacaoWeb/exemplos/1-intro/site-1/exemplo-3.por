/*
Escreva um programa que leia dois números inteiros e 
imprima na tela a soma deles.
*/

programa {
  funcao inicio() {

    //Declaração de variáveis
    inteiro num1
    inteiro num2
    inteiro resultado

    //Entrada de Dados
    escreva("Bem vindo a calculadora da 201!!")
    escreva("Digite o primeiro número:")
    leia(num1)

    escreva ("Digite o segundo:")
    leia(num2)

    //Processamento
    resultado = num1 + num2

    //Saida de dados
    escreva("O resultado da soma é: ", resultado, "!")
    
    
  }  
}