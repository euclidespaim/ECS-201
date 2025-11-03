var formulario  = document.getElementById("formulario")

var entrada = document.getElementById("entrada");
var saida = document.getElementById("saida");

formulario.addEventListener("submit", function(event) {

  event.preventDefault();
    
  var texto = entrada.value;
  
  saida.textContent = texto;
  saida.style.backgroundColor = "yellow";
  saida.style.padding = "10px";
});
