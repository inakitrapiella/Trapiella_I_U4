document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.getElementById("id_simulador");

    if (!formulario) return;

    formulario.addEventListener("submit", function (event) {

        event.preventDefault();

        const nombre = formulario.elements["nombre_apellido"].value.trim();
        const edad = parseInt(formulario.elements["edad"].value.trim());
        const email = formulario.elements["email"].value.trim();
        const celular = formulario.elements["celular"].value.trim();

        let errores = [];

        if (nombre.length < 3) errores.push("El nombre debe tener al menos 15 caracteres");
        if (isNaN(edad) || edad < 18) errores.push("Debes ser mayor de edad");
        if (!email.includes("@") || !email.includes(".")) errores.push("Correo electronico invalido");
        if (celular.length < 6) errores.push("Celular invalido");

        if (errores.length > 0) {
            mostrarErrores(errores);
        } else {
            formulario.submit();
        }
    });

    function mostrarErrores(listaErrores) {
        let div = document.querySelector(".mensaje-error-js");
        if (!div) {
            div = document.createElement("div");
            div.className = "mensaje-error-js";
            formulario.parentNode.insertBefore(div, formulario);
        }
        div.innerHTML = "<ul>" + listaErrores.map(err => `<li>${err}</li>`).join("") + "</ul>";
    }
});