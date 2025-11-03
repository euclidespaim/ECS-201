var count = 0;

document.getElementById('aumentar').addEventListener('click', function() {
  count = count + 1;
  document.getElementById('contador').innerText = count;
});

document.getElementById('diminuir').addEventListener('click', function() {
  count--;
  document.getElementById('contador').innerText = count;
});

document.getElementById('limpar').addEventListener('click', function() {
  count = 0;
  document.getElementById('contador').innerText = count;
});
