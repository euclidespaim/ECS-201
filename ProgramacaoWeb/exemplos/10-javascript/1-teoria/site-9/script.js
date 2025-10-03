var btn = document.getElementById("toggle");
var msg = document.getElementById("mensagem");

btn.onclick = function () {
  if (msg.style.display === "none") {
    msg.style.display = "block";
    btn.innerText = "Esconder";
  } else {
    msg.style.display = "none";
    btn.innerText = "Mostrar";
  }
};