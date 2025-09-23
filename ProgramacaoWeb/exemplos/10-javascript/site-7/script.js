// Pegamos os elementos do HTML
var lampada = document.getElementById("lampada");
var btnAcender = document.getElementById("acender");
var btnApagar = document.getElementById("apagar");

// Quando clicar em "Acender"
btnAcender.onclick = function() {
  lampada.src = "./img/lamp-on.png";
  lampada.alt = "Lâmpada acesa";
  lampada.style.marginRight = "3px";
};

// Quando clicar em "Apagar"
btnApagar.onclick = function() {
  lampada.src = "./img/lamp-off.png";
  lampada.alt = "Lâmpada apagada";
  lampada.style.marginRight = "0px";
};

