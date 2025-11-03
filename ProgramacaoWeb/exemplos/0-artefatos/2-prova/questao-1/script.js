var botaoMostrar = document.getElementById("mostrar");
var botaoEsconder = document.getElementById("esconder");
var texto = document.getElementById("texto");

// Mostra o parágrafo
botaoMostrar.addEventListener("click", function () {
  texto.style.display = "block";
});

// Esconde o parágrafo
botaoEsconder.addEventListener("click", function () {
  texto.style.display = "none";
});