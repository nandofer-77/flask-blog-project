"""
Definición de la instancia de Flask de nuestra aplicación
"""
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)   # Definición de la instancia de Flask de nuestra aplicación
# inicializar extensiones de Flask
app.config.from_object(Config)
database = SQLAlchemy(app)  # objeto que representa la base de datos
migrate = Migrate(app, database)    # representación del motor de migración

from app import routes, models
# models define la estructura de la base de datos