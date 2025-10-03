btn = document.getElementById('btn');

btn.addEventListener('click', function() {

    var input = document.getElementById('nome').value;
    
    document.getElementById('res').innerHTML = "Olá, " + input + "!";
});