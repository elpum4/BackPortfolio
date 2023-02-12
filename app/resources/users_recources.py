"""This file contains logic for /helloWorld, an endpoint to test the API."""

from flask_restful import Resource

# flask imports

# imports for PyJWT authentication
from app.common.authentication import token_required
from app.models.behaviour.user import UserController
from app.common.helpers import create_logger
from flask import jsonify, make_response


logger = create_logger()


class GetUser(Resource):
    @token_required
    def get(self, current_user):
        try:
            response = UserController.get_all_users()
            logger.info("Users list successfully retrieved")
        except Exception as e:
            # helpers.log_traceback(e)
            message = "Error retrieving the collections"
            logger.error(f"{message}. Error: {e}")
            return make_response(
                jsonify({"message": message}),
                400,
            )
        return response


class SignInUser(Resource):
    def post(self):
        try:
            response = UserController.login()
            logger.info("user successfully signin")
        except Exception as e:
            # helpers.log_traceback(e)
            message = "Error retrieving the user"
            logger.error(f"{message}. Error: {e}")
            return make_response(
                jsonify({"message": message}),
                400,
            )
        return response


class SignUpUser(Resource):
    def post(self):
        try:
            response = UserController.signup()
            logger.info("User signup successfully")
        except Exception as e:
            # helpers.log_traceback(e)
            message = "Don't signup user"
            logger.error(f"{message}. Error: {e}")
            return make_response(
                jsonify({"message": message}),
                400,
            )
        return response
