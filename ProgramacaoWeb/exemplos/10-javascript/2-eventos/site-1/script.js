var caixa = document.getElementById("box");

caixa.addEventListener("mouseover", function() {
  caixa.style.background = "purple";
});

caixa.addEventListener("mouseout", function() {
  caixa.style.background = "";
});