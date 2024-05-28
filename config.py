import os
directorio_base = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Configuracion de clave secreta
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-generica'
    
    # Configuración para Flask-SQL_Alchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(directorio_base, 'app.db')