//Archivo js con las funciones de validación

// ---------------------
// EJERCICIO 1 - validación para que el número ingresado esté dentro de un rango
// ---------------------
validateRange = (max, min, object) => {
    const evaluated = parseInt(object.value);
    max = parseInt(max);
    min = parseInt(min);

    if (isNaN(evaluated)) {
        alert("Por favor, ingresa un número válido.");
        object.value = '';
        return;
    }

    if (evaluated > max) {
        alert(`El valor ingresado (${evaluated}) es mayor a la nota máxima permitida (${max})`);
        object.value = '';
        return;
    }

    if (evaluated < min) {
        alert(`El valor ingresado (${evaluated}) es menor a la nota mínima permitida (${min})`);
        object.value = '';
        return;
    }
}

// ---------------------
// EJERCICIO 2 - Validar campos vacíos
// ---------------------
function validarCamposNombres() {
    const campos = ['nombre1', 'nombre2', 'nombre3'];

    for (let id of campos) {
        const valor = document.getElementById(id).value.trim();
        if (valor === '') {
            alert(`Por favor, completa el campo ${id}.`);
            return false;
        }
    }
    
    return true;
}
