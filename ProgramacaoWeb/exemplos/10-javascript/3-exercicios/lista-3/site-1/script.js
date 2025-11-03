const vermelho  = document.getElementById("vermelho");
const verde = document.getElementById("verde");
const azul = document.getElementById("azul");

vermelho.addEventListener("click", function() {
  document.body.style.backgroundColor = "red";
});

verde.addEventListener("click", function() {
  document.body.style.backgroundColor = "green";
});

azul.addEventListener("click", function() {
  document.body.style.backgroundColor = "blue";
});