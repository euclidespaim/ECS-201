// Pega os elementos
var btn = document.getElementById("toggle");
var img = document.getElementById("img");

// Quando clicar no botão
btn.onclick = function() {
  if (img.style.display === "none") {
    img.style.display = "block";   // mostra
  } else {
    img.style.display = "none";    // esconde
  }
};
