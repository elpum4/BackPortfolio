"""This module contains all controllers related to Entity base model."""
from __future__ import annotations

from typing import Text

from app.common.db_postgres import db
from app.common import helpers
from app.models.bases.experiencia import Experiencia, TipoExperiencia
from sqlalchemy.sql.sqltypes import DateTime, Boolean
from flask import request
import uuid

import dataclasses

logger = helpers.create_logger()


@dataclasses.dataclass
class ExpController(Experiencia, db.Model):

    """Manages and persist model object."""

    id: int
    exp_actual: Boolean
    exp_comienzo: DateTime
    exp_descripcion: Text
    exp_final: DateTime
    exp_sitio: Text
    exp_titulo: Text
    exp_urllogo: Text
    exp_tipo: int

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
        q = db.session.query(ExpController)

        try:
            results = q.all()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            raise Exception

        # Result as dict

        type = TipoExpController.get_all()
        d_type = {item["id"]: item["name"] for item in type}
        data = []
        for k in results:
            pre = k.to_dict()
            pre["exp_tipo"] = d_type.get(pre["exp_tipo"])
            data.append(pre)
        return data

    @classmethod
    def from_id(self, id):
        # querying the database
        # for all the entries in it
        q = db.session.query(ExpController).filter(ExpController.id == id)
        try:
            results = q.first()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            raise Exception

        # Result as dict

        type = TipoExpController.get_all()
        d_type = {item["id"]: item["name"] for item in type}

        pre = results.to_dict()
        pre["ed_tipo"] = d_type.get(pre["ed_tipo"])
        return pre

    @classmethod
    def delete(self, id):
        # querying the database
        # for all the entries in it
        q = db.session.query(ExpController).filter(ExpController.id == id)
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
        type = TipoExpController.get_all()
        d_type = {item["name"]: item["id"] for item in type}
        data["exp_tipo"] = d_type.get(data["exp_tipo"])

        # checking for existing user
        exp = ExpController(**data)
        exp.save_to_db()

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()


@dataclasses.dataclass
class TipoExpController(TipoExperiencia, db.Model):

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
        q = db.session.query(TipoExpController)

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
        education = TipoExpController(**data)
        education.save_to_db()

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
