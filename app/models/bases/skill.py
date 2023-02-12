"""This module contains the application models.

Each model is represented by a SQL table.
"""


from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import String, DateTime, Boolean

Base = declarative_base()


class Skill(Base):

    __tablename__ = "skill"

    id = Column(Integer, primary_key=True)
    sk_titulo = Column(String(50), default=None)
    sk_habilidad = Column(Integer, default=None)

    @staticmethod
    def get_dtypes_attribute_list():
        return dict(
            id=Integer,
            sk_titulo=String,
            sk_habilidad=Integer,
        )
