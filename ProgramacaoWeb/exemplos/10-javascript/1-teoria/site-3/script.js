document.getElementById("nome").onclick = function () {
  let nome = prompt("Digite seu nome:");
  document.getElementById("resposta").innerText = "Bem-vindo, " + nome + "!";
  
  console.log(nome);
};
