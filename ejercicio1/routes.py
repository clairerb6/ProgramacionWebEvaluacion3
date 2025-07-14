from flask import Blueprint, render_template, request
from .forms import FormularioNotas
from database import insertar_registro, obtener_registros

ej1 = Blueprint('ej1', __name__, template_folder='../templates/ejercicio1')

@ej1.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    form = FormularioNotas()
    resultado = None

    if form.validate_on_submit():
        nombre = form.nombre.data
        rut = form.rut.data
        nota1 = form.nota1.data
        nota2 = form.nota2.data
        nota3 = form.nota3.data
        asistencia = form.asistencia.data

        promedio = round((nota1 + nota2 + nota3) / 3, 1)
        estado = "✅ Aprobado" if promedio >= 40 and asistencia >= 75 else "❌ Reprobado"

        resultado = {
            "promedio": promedio,
            "estado": estado,
            "color": "text-success" if estado.startswith("✅") else "text-danger"
        }

        insertar_registro(nombre, rut, nota1, nota2, nota3, asistencia, promedio, estado)

    registros = obtener_registros()
    return render_template('ejercicio1.html', form=form, resultado=resultado, registros=registros)
