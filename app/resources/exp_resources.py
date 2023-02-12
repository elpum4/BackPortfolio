"""This file contains logic for /helloWorld, an endpoint to test the API."""

from flask_restful import Resource

# flask imports
from flask import jsonify, make_response

# imports for PyJWT authentication
from app.models.behaviour.experiencia import ExpController, TipoExpController
from app.common.helpers import create_logger
from app.common.authentication import token_required


logger = create_logger()


class AllExp(Resource):
    def get(self):
        try:
            response = ExpController.get_all()
            # logger.info("collection list successfully retrieved")
        except Exception as e:
            # helpers.log_traceback(e)
            message = "Error retrieving the exp list"
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
            response = ExpController.new()
            # logger.info("successfully created")
        except Exception as e:
            # helpers.log_traceback(e)
            message = "Error to created the exp list"
            logger.error(f"{message}. Error: {e}")
            return make_response(
                jsonify({"message": message}),
                400,
            )

        return make_response(
            jsonify({"Message": "Successfully"}),
            201,
        )


class Exp(Resource):
    def get(self, id):
        try:
            response = ExpController.from_id(id)
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
            response = ExpController.delete(id)
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


class AllTipoExp(Resource):
    def get(self):
        try:
            response = TipoExpController.get_all()
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
    def post(self, current_user):
        try:
            response = TipoExpController.new()
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
