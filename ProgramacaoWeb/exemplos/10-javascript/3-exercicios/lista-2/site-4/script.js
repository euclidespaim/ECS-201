var select = document.getElementById("select");
var saida = document.getElementById("saida");

select.addEventListener("change", function() {
  var emoji = select.value;
  saida.textContent = emoji;
});

