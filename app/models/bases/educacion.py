"""This module contains the application models.

Each model is represented by a SQL table.
"""

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import String, DateTime, Boolean
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class TipoEducacion(Base):

    __tablename__ = "tipo_educacion"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), default=None)

    @staticmethod
    def get_dtypes_attribute_list():
        return dict(
            id=Integer,
            name=String,
        )


class Educacion(Base):

    __tablename__ = "educacion"

    id = Column(
        Integer,
        primary_key=True,
    )
    ed_actual = Column(Boolean, default=False)
    ed_comienzo = Column(DateTime, default=None)
    ed_descripcion = Column(String(1000), default=None)
    ed_final = Column(DateTime, default=None)
    ed_institucion = Column(String(100), default=None)
    ed_titulo = Column(String(100), default=None)
    ed_urllogo = Column(String(1000), default=None)
    ed_tipo = Column(Integer, ForeignKey("tipo_educacion.id"))
    tipo = relationship(
        TipoEducacion, backref=backref("list_ed", uselist=True)
    )

    @staticmethod
    def get_dtypes_attribute_list():
        return dict(
            id=Integer,
            ed_actual=Boolean,
            ed_comienzo=DateTime,
            ed_descripcion=String,
            ed_final=DateTime,
            ed_institucion=String,
            ed_titulo=String,
            ed_urllogo=String,
            ed_tipo=Integer,
        )
