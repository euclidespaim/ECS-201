function adicionar() {
  var texto = document.getElementById('item').value;
  if (texto !== "") {
    var li = document.createElement('li');
    li.innerText = texto;
    document.getElementById('lista').appendChild(li);
    document.getElementById('item').value = "";
  }
}