var contador = 0;

const p = document.getElementById("contador");
const btnMais = document.getElementById("mais");
const btnMenos = document.getElementById("menos");

btnMais.onclick = function() {
  contador = contador + 1;
  p.textContent = contador;
}

btnMenos.onclick = function(){
  contador--
  p.textContent = contador
}