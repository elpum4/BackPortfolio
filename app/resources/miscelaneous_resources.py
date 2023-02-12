"""This file contains logic for /helloWorld, an endpoint to test the API."""

from flask_restful import Resource
from app.common.authentication import token_required
from flask import request, jsonify, make_response


class HelloWorld(Resource):
    """Class to define a Hello World API resource."""

    def get(self):
        """Gets a 'Hello World' message.

        This is the test zone. Put here any code you wish to test and send a
        request to this endpoint /helloWorld
        """
        return make_response(
            jsonify(
                {
                    "message": (
                        "Hello world!. This is a friendly greeting from"
                        "Portfolio API"
                    )
                }
            ),
            201,
        )


class HelloWorldProtected(Resource):
    """Class to define a protected Hello World API resource."""

    @token_required
    def get(self, current_user=None):
        """Gets an authenticated 'Hello World' message.

        This endpoint returns the email of the current user logged in. It's
        meant to test the login.
        """
        return make_response(
            jsonify(
                {"message": f"Hello {current_user}" "welcome to Portfolio API"}
            ),
            200,
        )
