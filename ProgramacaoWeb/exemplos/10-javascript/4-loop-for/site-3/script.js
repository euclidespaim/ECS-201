const nomes = [
  'Ana', 
  'João', 
  'Marcos', 
  'Mario', 
  'Pedro'
];

const mostrar = document.getElementById('mostrar');
const limpar = document.getElementById('limpar');
const lista = document.getElementById('lista');

mostrar.addEventListener('click', () => {
    lista.innerHTML = '';

    for (let i = 0; i < nomes.length; i++) {
      const item = document.createElement('li');
      item.textContent = nomes[i]
      lista.appendChild(item);
    }
});

limpar.addEventListener('click', () => {
    lista.innerHTML = '';
});