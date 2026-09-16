
document.addEventListener("DOMContentLoaded", function () {

    const cards = document.querySelectorAll(".about-card");

    cards.forEach(function (card) {

        card.addEventListener("click", function () {
            card.classList.toggle("active");
        });

    });

});

