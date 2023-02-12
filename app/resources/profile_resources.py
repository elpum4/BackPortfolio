"""This file contains logic for /helloWorld, an endpoint to test the API."""

from flask_restful import Resource

# flask imports
from flask import request, jsonify, make_response
import uuid  # for public id
from werkzeug.security import generate_password_hash, check_password_hash

# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta
from app.common.authentication import token_required
from app.models.behaviour.profile import ProfileController
from app.common.helpers import create_logger
from app.common.authentication import token_required
import json


logger = create_logger()


class AllProfile(Resource):
    def get(self):
        try:
            response = ProfileController.get_all()
            # logger.info("collection list successfully retrieved")
        except Exception as e:
            # helpers.log_traceback(e)
            message = "Error retrieving the profile list"
            logger.error(f"{message}. Error: {e}")
            return make_response(
                jsonify({"message": message}),
                400,
            )

        return make_response(
            jsonify({"response": response}),
            200,
        )

    @token_required
    def post(self, current_user):
        try:
            response = ProfileController.new()
            # logger.info("successfully created")
        except Exception as e:
            # helpers.log_traceback(e)
            message = "Error to created the profile list"
            logger.error(f"{message}. Error: {e}")
            return make_response(
                jsonify({"message": message}),
                400,
            )

        return make_response(
            jsonify({"Message": "Successfully"}),
            201,
        )


class Profile(Resource):
    def get(self, id):
        try:
            response = ProfileController.from_id(id)
            logger.info("collection list successfully retrieved")
        except Exception as e:
            # helpers.log_traceback(e)
            message = "Error retrieving the education list"
            logger.error(f"{message}. Error: {e}")
            return make_response(
                jsonify({"message": message}),
                400,
            )

        return make_response(
            jsonify({"response": response}),
            200,
        )

    @token_required
    def delete(self, current_user, id):
        try:
            response = ProfileController.delete(id)
            logger.info("successfully Created")
        except Exception as e:
            # helpers.log_traceback(e)
            message = "Error to created the education list"
            logger.error(f"{message}. Error: {e}")
            return make_response(
                jsonify({"message": message}),
                400,
            )

        return make_response(
            jsonify({"Message": "Successfully"}),
            201,
        )
