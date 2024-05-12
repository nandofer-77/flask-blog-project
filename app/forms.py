# importación de la clase base FlaskForm
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField
# el validador DataRequired permite revisar que el campo no se envía vacío
from wtforms.validators import DataRequired 

# formulario de inicio de sesion

class FormularioLogin(FlaskForm):
    """
    Clase para crear objetos de Formulario de inicio de sesion
    """
    usuario = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña',  validators=[DataRequired()])
    remember_me = BooleanField('Olvidaste tu contraseña?')
    submit = SubmitField('Iniciar sesión')