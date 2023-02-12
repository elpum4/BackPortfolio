"This module contains objects to set authentication processes."
from flask import request, jsonify, make_response

from functools import wraps
import jwt
from .api_connections import SECRET_KEY
from app.models.behaviour.user import UserController


# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if "X-Access-Token" in request.headers:
            token = request.headers["X-Access-Token"]
        # return 401 if token is not passed
        if not token:
            return make_response(
                jsonify({"message": "Token is missing !!"}), 401
            )

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = UserController.from_id(data["public_id"])
        except:
            return (
                make_response(jsonify({"message": "Token is invalid !!"})),
                401,
            )
        # returns the current logged in users contex to the routes
        return f(current_user, *args, **kwargs)

    return decorator
