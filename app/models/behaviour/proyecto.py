"""This module contains all controllers related to Entity base model."""
from __future__ import annotations

from typing import Text

from app.common.db_postgres import db
from app.common import helpers
from app.models.bases.proyecto import Proyecto, TipoProyecto
from flask import request

import dataclasses

logger = helpers.create_logger()


@dataclasses.dataclass
class ProyectoController(Proyecto, db.Model):

    """Manages and persist model object."""

    id: int
    proy_cliente: Text
    proy_descripcion: Text
    proy_titulo: Text
    proy_url: Text
    proy_urlimg: Text
    proy_categoria: int

    def to_dict(self):
        """Convert a controller to dictionary."""
        return {
            k: helpers.json_serial(v)
            for k, v in dataclasses.asdict(self).items()
        }

    @classmethod
    def get_all(self):
        # querying the database
        # for all the entries in it
        q = db.session.query(ProyectoController)

        try:
            results = q.all()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            raise Exception

        # Result as dict

        type = TipoProyController.get_all()
        d_type = {item["id"]: item["name"] for item in type}
        data = []
        for k in results:
            pre = k.to_dict()
            pre["proy_categoria"] = d_type.get(pre["proy_categoria"])
            data.append(pre)
        return data

    @classmethod
    def from_id(self, id):
        # querying the database
        # for all the entries in it
        q = db.session.query(ProyectoController).filter(
            ProyectoController.id == id
        )
        try:
            results = q.first()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            raise Exception

        # Result as dict

        type = TipoProyController.get_all()
        d_type = {item["id"]: item["name"] for item in type}

        pre = results.to_dict()
        pre["proy_categoria"] = d_type.get(pre["proy_categoria"])
        return pre

    @classmethod
    def delete(self, id):
        # querying the database
        # for all the entries in it
        q = db.session.query(ProyectoController).filter(
            ProyectoController.id == id
        )
        try:
            results = q.delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            raise Exception
        return results

    @classmethod
    def new(self):

        data = request.get_json()
        type = TipoProyController.get_all()
        d_type = {item["name"]: item["id"] for item in type}
        data["proy_categoria"] = d_type.get(data["proy_categoria"])

        # checking for existing user
        education = ProyectoController(**data)
        education.save_to_db()

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()


@dataclasses.dataclass
class TipoProyController(TipoProyecto, db.Model):

    """Manages and persist model object."""

    id: int
    name: Text

    def to_dict(self):
        """Convert a controller to dictionary."""
        return {
            k: helpers.json_serial(v)
            for k, v in dataclasses.asdict(self).items()
        }

    @classmethod
    def get_all(self):
        # querying the database
        # for all the entries in it
        q = db.session.query(TipoProyController)

        try:
            results = q.all()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            raise Exception

        # Result as dict
        data = []
        for k in results:
            data.append(k.to_dict())

        return data

    @classmethod
    def new(self):

        data = request.get_json()

        # checking for existing user
        education = TipoProyController(**data)
        education.save_to_db()

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
