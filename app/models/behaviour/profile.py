"""This module contains all controllers related to Entity base model."""
from __future__ import annotations

from typing import Text

from app.common.db_postgres import db
from app.common import helpers
from app.models.bases.profile import Profile
from flask import request

import dataclasses

logger = helpers.create_logger()


@dataclasses.dataclass
class ProfileController(Profile, db.Model):

    """Manages and persist model object."""

    id: int
    hd_nombre: Text
    hd_mail: Text
    hd_profesion: Text
    hd_sobremi: Text
    hd_urlbanner: Text
    hd_urlgit: Text
    hd_urllkd: Text
    hd_urlperfil: Text

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
        q = db.session.query(ProfileController)

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
    def from_id(self, id):
        # querying the database
        # for all the entries in it
        q = db.session.query(ProfileController).filter(
            ProfileController.id == id
        )
        print(q)
        try:
            results = q.first()
            print(results)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            raise Exception

        # Result as dict

        pre = results.to_dict()
        return pre

    @classmethod
    def delete(self, id):
        # querying the database
        # for all the entries in it
        q = db.session.query(ProfileController).filter(
            ProfileController.id == id
        )
        print(q)
        try:
            results = q.delete()
            print(results)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            raise Exception
        return results

    @classmethod
    def new(self):

        data = request.get_json()

        # checking for existing user
        education = ProfileController(**data)
        education.save_to_db()

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
