"""
Home page routes

Return complete HTML page from view function
"""
from flask import render_template, flash, redirect
from app import app
from app.forms import FormularioLogin


@app.route('/')
@app.route("/index")
def index():
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
    return render_template('index.html', usuario = usuario, posts=posts)

@app.route("/login", methods=['GET', 'POST']) # Funcion de visualizacion del inicio de sesion
def login():
    form = FormularioLogin()
    if form.validate_on_submit():   # flash permite recibir las credenciales de sesión
        flash(f'Login requested for user {form.usuario.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='Inicio de sesión', form=form)