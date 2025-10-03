var form = document.getElementById("form");

form.addEventListener("submit", function(e) {

  e.preventDefault(); // impede reload da página
  alert("Você digitou: " + document.getElementById("usuario").value);

});