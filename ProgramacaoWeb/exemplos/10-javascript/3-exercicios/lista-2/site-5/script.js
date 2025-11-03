var entrada = document.getElementById("entrada");

entrada.addEventListener("focus", function() {
  entrada.style.backgroundColor = "yellow";
});

entrada.addEventListener("blur", function() {
  entrada.style.backgroundColor = "white";
});

