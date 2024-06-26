"""
    definición de la estructura inicial de la base de datos
"""

from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sqa
import sqlalchemy.orm as sqo
from app import db

class Usuario(db.Model):
    # clase para representar a los usuarios guardados en la base de datos
    # la función sqo.mapped_column() permite agregar la configuración adicional para definir las columnas  de la base de datos

    id: sqo.Mapped[int] = sqo.mapped_column(primary_key=True)
    username: sqo.Mapped[str] = sqo.mapped_column(sqa.String(64), index=True, unique=True)
    email: sqo.Mapped[str] = sqo.mapped_column(sqa.String(120), index=True, unique=True)
    hash_password: sqo.Mapped[Optional[str]] = sqo.mapped_column(sqa.String(256))
    # type hint Optional[] permite definir un tipo de columna vacía o nullable en la base de datos

    posts: sqo.WriteOnlyMapped['Post'] = sqo.Relationship(back_populates='autor')

    def __repr__(self):
        # indica al interprete de python como imprimir objetos de esta clase

        return f"<User {self.username}>"

class Post(db.Model):
    
    id: sqo.Mapped[int] = sqo.mapped_column(primary_key=True)
    user_id: sqo.Mapped[int] = sqo.mapped_column(sqa.ForeignKey(Usuario.id), index=True)
    contenido: sqo.Mapped[str] = sqo.mapped_column(sqa.String(140))
    timestamp: sqo.Mapped[datetime] = sqo.mapped_column(index=True,
                                                         default=lambda: datetime.now(timezone.utc))
    autor: sqo.Mapped[Usuario] = sqo.relationship(back_populates='posts')

    def __repr__(self):
        return f"<Post {self.contenido}"