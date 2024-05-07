from flask_wtf import FlaskForm # importación de la clase base FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired # el validador permite revisar que el campo no se envía vacío

# formulario de inicio de sesion

class FormularioLogin(FlaskForm): # por cada campo, se crea un objeto de esta clase

    usuario     = StringField('Usuario', validators=[DataRequired()])
    password    = PasswordField('Contraseña',  validators=[DataRequired()])
    remember_me = BooleanField('Olvidaste tu contraseña?')
    submit      = SubmitField('Iniciar sesión')