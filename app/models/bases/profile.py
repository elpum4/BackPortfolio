"""This module contains the application models.

Each model is represented by a SQL table.
"""


from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import String

Base = declarative_base()


class Profile(Base):

    __tablename__ = "profile"

    id = Column(Integer, primary_key=True)
    hd_nombre = Column(String(50), default=None)
    hd_mail = Column(String(50), default=None)
    hd_profesion = Column(String(50), default=None)
    hd_sobremi = Column(String(1000), default=None)
    hd_urlbanner = Column(String(1000), default=None)
    hd_urlgit = Column(String(1000), default=None)
    hd_urllkd = Column(String(1000), default=None)
    hd_urlperfil = Column(String(1000), default=None)

    @staticmethod
    def get_dtypes_attribute_list():
        return dict(
            id=Integer,
            hd_nombre=String,
            hd_mail=String,
            hd_profesion=String,
            hd_sobremi=String,
            hd_urlbanner=String,
            hd_urlgit=String,
            hd_urllkd=String,
            hd_urlperfil=String,
        )
