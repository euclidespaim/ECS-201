const imagens = document.querySelector('.imagens');
const anterior = document.querySelector('.anterior');
const proximo = document.querySelector('.proximo');

let indice = 0;
const total = document.querySelectorAll('.imagens img').length;

function atualizarCarrossel() {
  const deslocamento = -indice * 100;
  imagens.style.transform = `translateX(${deslocamento}%)`;
}

proximo.addEventListener('click', () => {
  indice = (indice + 1) % total;
  atualizarCarrossel();
});

anterior.addEventListener('click', () => {
  indice = (indice - 1 + total) % total;
  atualizarCarrossel();
});

// Rolagem automática
setInterval(() => {
  indice = (indice + 1) % total;
  atualizarCarrossel();
}, 4000);
