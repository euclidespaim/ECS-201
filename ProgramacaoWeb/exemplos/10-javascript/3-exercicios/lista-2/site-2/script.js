lanterna = document.getElementById("lanterna");

lanterna.addEventListener("mouseover", function() {
    lanterna.src = "./img/lamp-on.png";
});

lanterna.addEventListener("mouseout", function() {
    lanterna.src = "./img/lamp-off.png";
});