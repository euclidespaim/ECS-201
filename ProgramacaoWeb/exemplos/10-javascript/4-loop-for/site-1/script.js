var botao = document.getElementById("botao");
var resultado = document.getElementById("resultado");


botao.addEventListener("click", async function() {
  resultado.innerHTML = "";

  for (var i = 1; i <= 10; i++) {
    resultado.textContent += i + " ";

    await(new Promise(resolve => setTimeout(resolve, 1000)));
  }

})