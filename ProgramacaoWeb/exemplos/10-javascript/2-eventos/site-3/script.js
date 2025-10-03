var select = document.getElementById("cores");

select.addEventListener("change", function () {
  document.body.style.background = select.value;
});