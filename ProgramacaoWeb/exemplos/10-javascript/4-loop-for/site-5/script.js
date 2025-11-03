const caixas = document.querySelectorAll('.caixa');
const botao = document.getElementById('botao');

const cores = [
  'red', 
  'blue', 
  'green', 
  'yellow', 
  'purple', 
  'orange',
  'pink',
  'brown',
  'gray',
  'cyan'
  ];

  botao.addEventListener('click', async () => { 
    for (let i = 0; i < caixas.length; i++) {

      const corAleatoria = cores[Math.floor(Math.random() * cores.length)];
      console.log(Math.random() * cores.length)

      caixas[i].style.backgroundColor = corAleatoria;

      await new Promise(resolve => setTimeout(resolve, 1000));
    }

  });