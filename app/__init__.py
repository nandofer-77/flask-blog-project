"""
Definición de la instancia de Flask de nuestra aplicación
"""
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes