"""This module contains all controllers related to Entity base model."""
from __future__ import annotations

from typing import Text

from app.common.db_postgres import db
from app.common import helpers
from app.models.bases.educacion import Educacion, TipoEducacion
from sqlalchemy.sql.sqltypes import DateTime, Boolean
from flask import request
import uuid

import dataclasses

logger = helpers.create_logger()


@dataclasses.dataclass
class EdController(Educacion, db.Model):

    """Manages and persist model object."""

    id: int
    ed_actual: Boolean
    ed_comienzo: DateTime
    ed_descripcion: Text
    ed_final: DateTime
    ed_institucion: Text
    ed_titulo: Text
    ed_urllogo: Text
    ed_tipo: int

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
        q = db.session.query(EdController)
        try:
            results = q.all()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            raise Exception

        # Result as dict

        type = TipoEdController.get_all()
        d_type = {item["id"]: item["name"] for item in type}

        data = []
        for k in results:
            pre = k.to_dict()
            pre["ed_tipo"] = d_type.get(pre["ed_tipo"])
            data.append(pre)
        return data

    @classmethod
    def from_id(self, id):
        # querying the database
        # for all the entries in it
        q = db.session.query(EdController).filter(EdController.id == id)
        try:
            results = q.first()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            raise Exception

        # Result as dict

        type = TipoEdController.get_all()
        d_type = {item["id"]: item["name"] for item in type}

        pre = results.to_dict()
        pre["ed_tipo"] = d_type.get(pre["ed_tipo"])
        return pre

    @classmethod
    def delete(self, id):
        # querying the database
        # for all the entries in it
        q = db.session.query(EdController).filter(EdController.id == id)
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
        type = TipoEdController.get_all()
        d_type = {item["name"]: item["id"] for item in type}
        data["ed_tipo"] = d_type.get(data["ed_tipo"])

        # checking for existing user
        education = EdController(**data)
        education.save_to_db()

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()


@dataclasses.dataclass
class TipoEdController(TipoEducacion, db.Model):

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
        q = db.session.query(TipoEdController)

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
        education = TipoEducacion(**data)
        education.save_to_db()

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
