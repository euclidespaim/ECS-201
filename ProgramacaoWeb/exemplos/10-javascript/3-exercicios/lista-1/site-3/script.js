// Quadrado de um número
// Crie um campo de entrada (input) para o usuário digitar um número.
// Ao clicar no botão, mostre no parágrafo:
// "O quadrado de X é Y".

btn = document.getElementById('btn') 

btn.addEventListener('click', function() {
    var input = document.getElementById('num').value;
    var resultado = input ** 2;

    document.getElementById('resultado').innerHTML = "O quadrado de " + input + " é " + resultado;
});