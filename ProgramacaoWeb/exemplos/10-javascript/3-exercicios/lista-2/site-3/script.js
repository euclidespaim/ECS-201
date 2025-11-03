const entrada = document.getElementById('entrada');
const saida = document.getElementById('saida');

entrada.addEventListener('keyup', () => {
  saida.textContent = entrada.value.toUpperCase();
});