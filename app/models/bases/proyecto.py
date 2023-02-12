"""This module contains the application models.

Each model is represented by a SQL table.
"""
import enum

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import String, DateTime, Boolean
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class TipoProyecto(Base):

    __tablename__ = "tipo_proyecto"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), default=None)

    @staticmethod
    def get_dtypes_attribute_list():
        return dict(
            id=Integer,
            name=String,
        )


class Proyecto(Base):

    __tablename__ = "proyecto"

    id = Column(Integer, primary_key=True)
    proy_cliente = Column(String(100), default=None)
    proy_descripcion = Column(String(1000), default=None)
    proy_titulo = Column(String(100), default=None)
    proy_url = Column(String(1000), default=None)
    proy_urlimg = Column(String(1000), default=None)
    proy_categoria = Column(Integer, ForeignKey("tipo_proyecto.id"))
    categoria = relationship(
        TipoProyecto, backref=backref("list_cat", uselist=True)
    )

    @staticmethod
    def get_dtypes_attribute_list():
        return dict(
            id=Integer,
            proy_cliente=String,
            proy_descripcion=DateTime,
            proy_titulo=String,
            proy_url=String,
            proy_urlimg=String,
            proy_categoria=Integer,
        )
