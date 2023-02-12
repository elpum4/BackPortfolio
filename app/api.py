"""This file contains the api APP and the routes"""
import datetime
import os

# frameworks & online resource access permission:
import flask
import flask_cors
import flask_jwt_extended
import flask_restful
from app.common.helpers import RequestFormatter

from flask.logging import default_handler
from app.common.db_postgres import db
from app.common import api_connections
from app.resources import miscelaneous_resources
from app.resources import (
    exp_resources,
    ed_resources,
    users_recources,
    profile_resources,
    proyecto_resources,
    skill_resources,
)

# API Environment
DATABASE_URL = api_connections.DATABASE_URL


# App creation
app = flask.Flask(__name__)
app.config["SECRET_KEY"] = api_connections.SECRET_KEY
# default CORS config, which allows requests from all origins (doesn't filter
# anything)
flask_cors.CORS(app)

# app config:
app.config["BUNDLE_ERRORS"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

# token config:
# Setup the Flask-JWT-Extended extension
# app.config['JWT_SECRET_KEY'] = config.SECRET_KEY
# default token expiration times
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=20)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = datetime.timedelta(minutes=40)
# Blacklisting of tokens
app.config["JWT_BLACKLIST_ENABLED"] = True
# specify what kind of tokens to check against the blacklist
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]
# Propagate exceptions so that they are re-raised rather than being handled by
# the app's error handlers. For example, this fixes the bug that nginx would
# return an error 500 instead of the true 401.
app.config["PROPAGATE_EXCEPTIONS"] = True

# token manager:
jwt = flask_jwt_extended.JWTManager(app)

# Flask_restful setup

api = flask_restful.Api(app, prefix="")

# test URIs:
api.add_resource(miscelaneous_resources.HelloWorld, "/api/hello_world")
api.add_resource(
    miscelaneous_resources.HelloWorldProtected, "/api/hello_world_protected"
)
api.add_resource(profile_resources.AllProfile, "/api/profile")
api.add_resource(profile_resources.Profile, "/api/profile/<string:id>")

api.add_resource(users_recources.GetUser, "/api/auth/get_users")
api.add_resource(users_recources.SignInUser, "/api/auth/signin")
api.add_resource(users_recources.SignUpUser, "/api/auth/signup")


api.add_resource(exp_resources.AllExp, "/api/experiencia")
api.add_resource(exp_resources.Exp, "/api/experiencia/<string:id>")
api.add_resource(exp_resources.AllTipoExp, "/api/tipoexperiencia")

api.add_resource(ed_resources.AllEd, "/api/educacion")
api.add_resource(ed_resources.Ed, "/api/educacion/<string:id>")
api.add_resource(ed_resources.AllTipoEd, "/api/tipoeducacion")

api.add_resource(proyecto_resources.AllProyecto, "/api/proyecto")
api.add_resource(proyecto_resources.Proyecto, "/api/proyecto/<string:id>")
api.add_resource(proyecto_resources.AllTipoProy, "/api/tipoproyecto")

api.add_resource(skill_resources.AllSkill, "/api/skill")
api.add_resource(skill_resources.Skill, "/api/skill/<string:id>")


formatter = RequestFormatter(
    "[%(asctime)s] %(remote_addr)s requested %(url)s\n"
    "%(levelname)s in %(module)s: %(message)s"
)
default_handler.setFormatter(formatter)

db.init_app(app)

if __name__ == "__main__":
    app.run()
