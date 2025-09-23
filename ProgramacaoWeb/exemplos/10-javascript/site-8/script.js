document.getElementById("sortear").onclick = function () {
  var numero = Math.floor(Math.random() * 10) + 1;
  document.getElementById("resultado").innerText = "Número sorteado: " + numero;
};
