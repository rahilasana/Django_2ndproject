
document.addEventListener("DOMContentLoaded", function () {

    const button = document.querySelector(".change-btn");
    const heading = document.querySelector(".home-content h1");

    button.addEventListener("click", function () {
        heading.textContent = "Welcome to Little Stars!";
    });

});
