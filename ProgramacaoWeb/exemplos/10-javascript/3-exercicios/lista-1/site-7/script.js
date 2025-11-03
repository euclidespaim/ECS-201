const entrada = document.getElementById("entrada");
const botao = document.getElementById("adicionar");
const lista = document.getElementById("lista");

botao.addEventListener("click", function() {
  const texto = entrada.value.trim();

  if (texto === "") return; // ignora entradas vazias

  const item = document.createElement("li");
  item.textContent = texto;

  lista.appendChild(item);
  entrada.value = ""; // limpa o campo
  entrada.focus(); // mantém o foco no input
});
