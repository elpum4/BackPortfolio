"""This module contains the application models.

Each model is represented by a SQL table.
"""


from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import String
import uuid

Base = declarative_base()


class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    public_id = Column(String(50))
    email = Column(String(50), default=None)
    password = Column(String(100), default=None)
    username = Column(String(50), default=None)
    admin = Column(Boolean, default=False)

    @staticmethod
    def get_dtypes_attribute_list():
        return dict(
            id=Integer,
            public_id=String,
            email=String,
            password=String,
            username=String,
            admin=Boolean,
        )
