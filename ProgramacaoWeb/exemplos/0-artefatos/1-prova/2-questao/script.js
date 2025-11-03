var botao = document.getElementById("botao");
var contador = 0;

botao.addEventListener("click", function () {
  contador = contador + 1;
  console.log(contador)

  if (contador < 5) {
    botao.textContent = "Cliques: " + contador;
  } else {
    botao.textContent = "Limite atingido!";
    botao.disabled = true; // desativa o botão
  }
});
