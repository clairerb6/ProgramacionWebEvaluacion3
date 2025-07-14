from flask import Blueprint, render_template
from .forms import FormularioNombres
from database import insertar_comparacion, obtener_comparaciones

ej2 = Blueprint('ej2', __name__, template_folder='../templates/ejercicio2')

@ej2.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    form = FormularioNombres()
    resultado = None

    if form.validate_on_submit():
        nombre1 = form.nombre1.data.strip()
        nombre2 = form.nombre2.data.strip()
        nombre3 = form.nombre3.data.strip()

        nombres = [nombre1, nombre2, nombre3]
        nombre_mayor = max(nombres, key=len)
        longitud = len(nombre_mayor)

        resultado = {
            "nombre": nombre_mayor,
            "longitud": longitud
        }

        insertar_comparacion(nombre1, nombre2, nombre3, nombre_mayor, longitud)

    comparaciones = obtener_comparaciones()
    return render_template('ejercicio2.html', form=form, resultado=resultado, comparaciones=comparaciones)
