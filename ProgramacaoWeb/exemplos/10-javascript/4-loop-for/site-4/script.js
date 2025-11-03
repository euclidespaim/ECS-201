const lista = document.getElementById('lista');

for (let i = 1; i <=10; i++) {
  const item = document.createElement('li')

  item.textContent = "O quadrado de " + i + " é " + (i * i);

  lista.appendChild(item);
}