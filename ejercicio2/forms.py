from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class FormularioNombres(FlaskForm):
    nombre1 = StringField('Nombre 1', validators=[DataRequired()])
    nombre2 = StringField('Nombre 2', validators=[DataRequired()])
    nombre3 = StringField('Nombre 3', validators=[DataRequired()])
