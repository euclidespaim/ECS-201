var botao = document.getElementById("botao");
var contador = 0;

// Adiciona o evento de clique
botao.addEventListener("click", function () {
  contador++;

  if (contador < 5) {
    botao.textContent = "Cliques: " + contador;
  } else {
    window.alert("Limite atingido!");
    botao.disabled = true;
    botao.textContent = "Limite atingido!";
  }
});