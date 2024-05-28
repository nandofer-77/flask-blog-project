'''
1- uso de decorador @app.shell_context_processor

'''
import sqlalchemy as sqa
import sqlalchemy.orm as sqo
from app import app, db
from app.models import Usuario, Post

@app.shell_context_processor
def make_shell_context():
    return {'sqa':sqa, 'sqo':sqo, 'db':db, 'Usuario':Usuario, 'Post':Post}

def main():
    pass

if __name__ == "__main__":
    main()
