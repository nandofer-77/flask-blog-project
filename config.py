import os

# Configuracion de clave secreta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bateria-de-sodio'