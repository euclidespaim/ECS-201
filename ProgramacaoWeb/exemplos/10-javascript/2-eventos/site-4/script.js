var campo = document.getElementById("nome");

campo.addEventListener("focus", function () {
  campo.style.border = "3px dotted blue";
});

campo.addEventListener("blur", function () {
  campo.style.border = "";
});