
document.addEventListener("DOMContentLoaded", function () {

    const cards = document.querySelectorAll(".service-card");

    cards.forEach(function (card) {

        card.addEventListener("click", function () {

            const title = card.querySelector("h2").textContent;

            alert("You selected: " + title);

        });

    });

});

