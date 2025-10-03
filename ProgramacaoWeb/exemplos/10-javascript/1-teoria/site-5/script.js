document.getElementById("somar").onclick = function () {

  let n1 = document.getElementById("n1").value;
  let n2 = document.getElementById("n2").value;

  let somar = Number(n1) + Number(n2);

  document.getElementById("resultado").innerText = "Resultado " + somar
}

document.getElementById("subtrair").onclick = function () {

  let n1 = document.getElementById("n1").value;
  let n2 = document.getElementById("n2").value;

  let subtrair = Number(n1) - Number(n2);

  document.getElementById("resultado").innerText = "Resultado " + subtrair
}

document.getElementById("dividir").onclick = function () {

  let n1 = document.getElementById("n1").value;
  let n2 = document.getElementById("n2").value;

  let dividir = Number(n1) / Number(n2);

  document.getElementById("resultado").innerText = "Resultado " + dividir
}

document.getElementById("multiplicar").onclick = function () {

  let n1 = document.getElementById("n1").value;
  let n2 = document.getElementById("n2").value;

  let multiplicar = Number(n1) * Number(n2);

  document.getElementById("resultado").innerText = "Resultado " + multiplicar
}


