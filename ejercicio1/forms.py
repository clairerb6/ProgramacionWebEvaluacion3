from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class FormularioNotas(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    rut = StringField('RUT', validators=[DataRequired()])
    nota1 = IntegerField('Nota 1', validators=[DataRequired(), NumberRange(min=10, max=70)])
    nota2 = IntegerField('Nota 2', validators=[DataRequired(), NumberRange(min=10, max=70)])
    nota3 = IntegerField('Nota 3', validators=[DataRequired(), NumberRange(min=10, max=70)])
    asistencia = IntegerField('Asistencia (%)', validators=[DataRequired(), NumberRange(min=0,  max=100)])
