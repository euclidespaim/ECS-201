const entrada = document.getElementById("entrada");
const saida = document.getElementById("saida");

entrada.addEventListener("keydown", function () {

  saida.textContent = entrada.value.length;

});