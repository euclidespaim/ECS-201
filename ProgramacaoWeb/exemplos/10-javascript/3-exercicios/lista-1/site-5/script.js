var cores = [
  'lightblue', 
  'lightgreen', 
  'lightpink', 
  'lightyellow', 
  'lightgray',
  'purple',
  'lightcoral', 
  'lightseagreen',
  'lightsalmon',
  'lightgoldenrodyellow'
]

document.getElementById('btn').onclick = function() {

  var corAleatoria = cores[Math.floor(Math.random() * cores.length)];
  
  console.log(corAleatoria);

  document.body.style.backgroundColor = corAleatoria;
 }
