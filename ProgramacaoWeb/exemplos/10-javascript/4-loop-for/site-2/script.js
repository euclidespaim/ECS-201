var entrada = document.getElementById("entrada");
var botao = document.getElementById("botao");
var lista = document.getElementById("lista");

botao.addEventListener("click", function() {
  lista.innerHTML = "";
  var numero = Number(entrada.value);

  for (let i = 1; i <= 10; i++) {
    var item = document.createElement("li");
    item.textContent = numero + " x " + i + " = " + (numero * i);
    lista.appendChild(item);

  }

});