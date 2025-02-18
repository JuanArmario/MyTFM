function loadPage(page) {
    document.getElementById("contentFrame").src = page;

    // Solo cerrar el menú si el elemento seleccionado es una hoja (sin submenús)
    if (!document.querySelector(`[onclick="loadPage('${page}')"]`).parentElement.classList.contains("submenu")) {
        closeMenu();
    }
}

function loadPDF() {
    closeMenu(); // Cerrar menú al seleccionar Thesis

    let iframe = document.getElementById("contentFrame");

    // Mostrar mensaje de carga antes de cargar el PDF
    iframe.outerHTML = `<div id="pdfLoadingMessage" class="loading-message">Loading PDF...</div>`;

    // Esperar un pequeño tiempo antes de cargar el PDF con Google Docs Viewer
    setTimeout(() => {
        let newIframe = document.createElement("iframe");
        newIframe.id = "contentFrame";
        newIframe.src = "https://docs.google.com/gview?url=https://juanarmario.github.io/MyTFM/Thesis/Thesis.pdf&embedded=true";
        newIframe.style.width = "100%";
        newIframe.style.height = "100%";
        newIframe.style.border = "none";

        // Reemplazar el mensaje con el iframe del PDF
        document.querySelector(".content").innerHTML = "";
        document.querySelector(".content").appendChild(newIframe);

        // Intentar recargar si el PDF no se muestra bien
        newIframe.onload = function () {
            setTimeout(() => {
                if (newIframe.contentWindow.document.body.innerHTML.length < 50) {
                    newIframe.src += "";
                }
            }, 1000);
        };
    }, 1000); // Pequeño retraso para mejorar la UX
}

// FUNCIÓN PARA CERRAR EL MENÚ
function closeMenu() {
    document.querySelector(".sidebar").classList.remove("active");
}

// FUNCIÓN PARA MANEJAR EL RESALTADO DE MENÚ
function highlightMenuItem(selectedItem) {
    // Quitar la clase 'active-item' de todos los elementos del menú
    document.querySelectorAll(".sidebar-links a").forEach(item => {
        item.classList.remove("active-item");
    });

    // Agregar la clase al elemento seleccionado
    selectedItem.classList.add("active-item");
}

document.addEventListener("DOMContentLoaded", function () {
    // Manejo de submenús desplegables
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

    // Cerrar menú solo si se selecciona una hoja (elemento sin submenús)
    document.querySelectorAll(".sidebar-links a").forEach(link => {
        link.addEventListener("click", function () {
            let parentLi = this.parentElement;

            // Solo cierra el menú si el elemento NO tiene un submenú dentro
            if (!parentLi.classList.contains("submenu") && !parentLi.parentElement.classList.contains("submenu-content")) {
                closeMenu();
            }

            highlightMenuItem(this); // Resaltar opción seleccionada
        });
    });

    // Cerrar menú cuando se haga clic fuera de él
    document.addEventListener("click", function (event) {
        const sidebar = document.querySelector(".sidebar");
        const menuToggle = document.querySelector(".menu-toggle");

        if (!sidebar.contains(event.target) && !menuToggle.contains(event.target)) {
            closeMenu();
        }
    });

    // Botón de menú para abrir/cerrar en móviles
    document.querySelector(".menu-toggle").addEventListener("click", function () {
        document.querySelector(".sidebar").classList.toggle("active");
    });
});