const numero = document.getElementById('numero');
const btn = document.getElementById('btn');
const resultado = document.getElementById('resultado');


btn.addEventListener('click', () => {
  const n = parseInt(numero.value);
  resultado.innerHTML = '';

  if (n % 2 === 0) {
    resultado.textContent = 'O número é par.';
  } else {
    resultado.textContent = 'O número é ímpar.';
  }
})