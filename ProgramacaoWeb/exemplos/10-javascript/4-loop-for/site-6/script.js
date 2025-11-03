const botao = document.getElementById('botao');
const contador = document.getElementById('contador');

botao.addEventListener('click', async () => {
  
  for (let i = 10; i > 0; i--) {
    contador.textContent = '';
    contador.textContent += i + ' ';

    await new Promise(resolve => setTimeout(resolve, 1000));
  }

  contador.textContent = 'Fogo! \u{1f680}';
});