function loadPage(page) {
    document.getElementById("contentFrame").src = page;
}

function loadPDF() {
    document.getElementById("contentFrame").src = "https://github.com/JuanArmario/MyTFM/blob/e5dccd1d3eec6652c93fe4674c5a1ef82a1ab0a4/Thesis/Machine%20Learning%20vs%20Deep%20Learning%20En%20la%20Detecci%C3%B3n%20del%20C%C3%A1ncer%20de%20H%C3%ADgado.pdf";
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


