"""This module contains all controllers related to Entity base model."""
from __future__ import annotations

import uuid
from typing import Text
import jwt
from app.common.db_postgres import db
from app.common import helpers
from app.models.bases.users import Users
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify, make_response
from datetime import datetime, timedelta
from app.common import api_connections
import dataclasses

logger = helpers.create_logger()


@dataclasses.dataclass
class UserController(Users, db.Model):

    id: int
    public_id: Text
    email: Text
    password: Text
    username: Text
    admin: bool

    def to_dict(self):
        """Convert a controller to dictionary."""
        return {
            k: helpers.json_serial(v)
            for k, v in dataclasses.asdict(self).items()
        }

    @classmethod
    def _new_id(cls) -> str:
        """Generates a new id."""
        while True:
            _id = str(uuid.uuid4())
            if cls._check_good_id(_id):
                return _id

    @staticmethod
    def _check_good_id(_id: str) -> bool:
        """Checks if ID already exists in database.

        Args:
            _id: The immutable ID of the object.
        Returns:
            True if there is not _id registered
        """
        try:
            db.session.query(UserController).filter(
                UserController.public_id == _id
            ).one()
        except NoResultFound as e:
            db.session.rollback()
            return True
        return False

    def from_id(id: str):
        """Checks if ID already exists in database.

        Args:
            _id: The immutable ID of the object.
        Returns:
            True if there is not _id registered
        """
        try:
            user = (
                db.session.query(UserController)
                .filter(UserController.public_id == id)
                .first()
            )
        except NoResultFound as e:
            db.session.rollback()
            return False
        return user

    def get_all_users():
        # querying the database
        # for all the entries in it
        users = db.session.query(UserController).all()
        # converting the query objects
        # to list of jsons
        output = []
        for user in users:
            # appending the user data json
            # to the response list
            user_data = {}
            user_data["public_id"] = user.public_id
            user_data["username"] = user.username
            user_data["password"] = user.password
            user_data["admin"] = user.admin
            output.append(user_data)

        return make_response(jsonify({"users": output}), 201)

        # route for logging user in

    def login():
        # creates dictionary of form data
        auth = request.get_json()

        if not auth or not auth.get("username") or not auth.get("password"):
            # returns 401 if any username or / and password is missing
            return make_response(
                "Could not verify",
                401,
                {"WWW-Authenticate": 'Basic realm ="Login required !!"'},
            )

        user = (
            db.session.query(UserController)
            .filter(UserController.username == auth.get("username"))
            .first()
        )
        logger.info(f"USER: {user}")
        if not user:
            # returns 401 if user does not exist
            return make_response(
                "Could not verify",
                401,
                {"WWW-Authenticate": 'Basic realm ="User does not exist !!"'},
            )

        if check_password_hash(user.password, auth.get("password")):
            # generates the JWT Token
            token = jwt.encode(
                {
                    "public_id": user.public_id,
                    "exp": datetime.utcnow() + timedelta(minutes=30),
                },
                api_connections.SECRET_KEY,
                "HS256",
            )

            return make_response(
                jsonify(
                    {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "accessToken": token,
                        "roles": [user.admin],
                        "tokenType": "X-Access-Token",
                    }
                ),
                200,
            )
        # returns 403 if password is wrong
        return make_response(
            "Could not verify",
            403,
            {"WWW-Authenticate": 'Basic realm ="Wrong Password !!"'},
        )

    # signup route
    def signup():
        data = request.get_json()
        hashed_password = generate_password_hash(
            data["password"], method="sha256"
        )

        # checking for existing user
        user = (
            db.session.query(UserController)
            .filter(UserController.email == data.get("email"))
            .first()
        )
        logger.info(f"Match user: {user}")
        if not user:
            # database ORM object
            user_controller = UserController(
                public_id=str(uuid.uuid4()),
                username=data["username"],
                email=data["email"],
                password=hashed_password,
                admin=data["admin"] or False,
            )
            # insert user
            logger.info(f"USER CONTROLLER: {user_controller}")
            user_controller.save_to_db()

            return make_response("Successfully registered.", 201)
        else:
            # returns 202 if user already exists
            return make_response("User already exists. Please Log in.", 202)

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
