const form = document.getElementById('formLista'); 
const campo = document.getElementById('campoItens');
const lista = document.getElementById('listaItens');

form.addEventListener('submit', (e)=> {
  e.preventDefault();
  lista.innerHTML = '';

  const itens = campo.value.split(',');
  console.log(itens);

  for (let n = 0; n < itens.length; n++) {
    const li = document.createElement('li');
    
    li.textContent = itens[n].trim();
    lista.appendChild(li);
    console.log(li);  
  }

  campo.value = '';
})