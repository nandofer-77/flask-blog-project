"""
Rutas o URIs del proyecto

Retorna las paginas HTML de las view function
"""
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import FormularioLogin


@app.route('/')
@app.route("/index")
# pagina de inicio
def index():
    # solución temporal a no tener una base de datos de publicaciones
    # se crean variables de ejemplo o placeholders
    usuario = {'username':'Fernando Javier'}
    posts = [
        {
        'autor': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
        },
        {
        'autor': {'username': 'Susan'},
        'body': 'The Avengers movie!'
        }
    ]
    return render_template('index.html', usuario=usuario, posts=posts)

@app.route("/login", methods=['GET', 'POST']) 
# Funcion de visualizacion del inicio de sesion
def login():
    form = FormularioLogin()
    if form.validate_on_submit():
        
        # flash permite mostrar un mensaje al usuario
        # se usa en este caso como una solución temporal a no tener un inicio de sesión, mostrando que la aplicación recibió las credenciales

        flash(f'Login requested for user {form.usuario.data}, remember_me={form.remember_me.data}')

        return redirect(url_for('index'))
        # redirect() instruye al navegador que cargue automaticamente la página del argumento

    return render_template('login.html', title='Inicio de sesión', form=form)