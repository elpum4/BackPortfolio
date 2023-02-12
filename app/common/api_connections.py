"""This file stores parameters needed by the flask rest api."""
import os

SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_URL = os.environ.get("DATABASE_URL")
