function loadPage(page) {
    document.getElementById("contentFrame").src = page;
}

function loadPDF() {
    document.getElementById("contentFrame").src = "https://JuanArmario.github.io/MyTFM/Thesis/Thesis.pdf";
}

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".submenu > a").forEach(menu => {
        menu.addEventListener("click", function (e) {
            e.preventDefault();
            let subMenu = this.nextElementSibling;
            let icon = this.querySelector(".toggle-icon");

            if (subMenu.style.display === "block") {
                subMenu.style.display = "none";
                icon.classList.remove("rotated");
            } else {
                subMenu.style.display = "block";
                icon.classList.add("rotated");
            }
        });
    });

    document.querySelector(".menu-toggle").addEventListener("click", function () {
        document.querySelector(".sidebar").classList.toggle("active");
    });
});
