var campo = document.getElementById("campo");

campo.addEventListener("keyup", function () {
  
  document.getElementById("saida").textContent = campo.value;
});