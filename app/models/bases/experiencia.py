"""This module contains the application models.

Each model is represented by a SQL table.
"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import String, DateTime, Boolean
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class TipoExperiencia(Base):

    __tablename__ = "tipo_experiencia"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), default=None)

    @staticmethod
    def get_dtypes_attribute_list():
        return dict(
            id=Integer,
            name=String,
        )


class Experiencia(Base):

    __tablename__ = "experiencia"

    id = Column(
        Integer,
        primary_key=True,
    )
    exp_actual = Column(Boolean, default=False)
    exp_comienzo = Column(DateTime, default=None)
    exp_descripcion = Column(String(1000), default=None)
    exp_final = Column(DateTime, default=None)
    exp_sitio = Column(String(100), default=None)
    exp_titulo = Column(String(100), default=None)
    exp_urllogo = Column(String(1000), default=None)
    exp_tipo = Column(Integer, ForeignKey("tipo_experiencia.id"))
    tipo = relationship(
        TipoExperiencia,
        backref=backref("list_exp", uselist=True),
    )

    @staticmethod
    def get_dtypes_attribute_list():
        return dict(
            id=Integer,
            exp_actual=Boolean,
            exp_comienzo=DateTime,
            exp_descripcion=String,
            exp_final=DateTime,
            exp_institucion=String,
            exp_titulo=String,
            exp_urllogo=String,
            exp_tipo=Integer,
        )
