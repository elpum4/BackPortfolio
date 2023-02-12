"""This file contains logic for /helloWorld, an endpoint to test the API."""

from flask_restful import Resource

# flask imports
from flask import jsonify, make_response

# imports for PyJWT authentication
from app.common.authentication import token_required
from app.models.behaviour.proyecto import (
    ProyectoController,
    TipoProyController,
)
from app.common.helpers import create_logger
from app.common.authentication import token_required


logger = create_logger()


class AllProyecto(Resource):
    def get(self):
        try:
            response = ProyectoController.get_all()
            # logger.info("collection list successfully retrieved")
        except Exception as e:
            # helpers.log_traceback(e)
            message = "Error retrieving the project list"
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
            response = ProyectoController.new()
            # logger.info("successfully created")
        except Exception as e:
            # helpers.log_traceback(e)
            message = "Error to created the project"
            logger.error(f"{message}. Error: {e}")
            return make_response(
                jsonify({"message": message}),
                400,
            )

        return make_response(
            jsonify({"Message": "Successfully"}),
            201,
        )


class Proyecto(Resource):
    def get(self, id):
        try:
            response = ProyectoController.from_id(id)
            logger.info("collection list successfully retrieved")
        except Exception as e:
            # helpers.log_traceback(e)
            message = f"Error retrieving the project id: {id}"
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
            response = ProyectoController.delete(id)
            logger.info("successfully Created")
        except Exception as e:
            # helpers.log_traceback(e)
            message = "Error to delte project"
            logger.error(f"{message}. Error: {e}")
            return make_response(
                jsonify({"message": message}),
                400,
            )

        return make_response(
            jsonify({"Message": "Successfully"}),
            201,
        )


class AllTipoProy(Resource):
    def get(self):
        try:
            response = TipoProyController.get_all()
            logger.info("collection list successfully retrieved")
        except Exception as e:
            # helpers.log_traceback(e)
            message = "Error retrieving the project list"
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
            response = TipoProyController.new()
            logger.info("successfully Created")
        except Exception as e:
            # helpers.log_traceback(e)
            message = "Error to created the project"
            logger.error(f"{message}. Error: {e}")
            return make_response(
                jsonify({"message": message}),
                400,
            )

        return make_response(
            jsonify({"Message": "Successfully"}),
            201,
        )
