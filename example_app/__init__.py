#!/bin/python3
from flask import Flask
import os
from dotenv import load_dotenv
import logging

# I find it helpful to define the root path of the app here
# You can use this to assign relative paths for file routing / .env loading / etc.
here = os.path.abspath(os.path.dirname(__file__))

# Path to .env file
env_path = os.path.join(here, ".env")

# Validate - if the path is valid we'll load the .env to use
if not os.path.exists(env_path):
    raise OSError("Whoa there! Looks like we're missing a .env file Cowboy")
else:
    load_dotenv(env_path)

# Setup logger
logging.basicConfig(level=logging.INFO)

##########


def create_app():
    """
    This helper function creates the Flask app. It is
    imported by the wsgi.py in the project root directory
    where it can be run on a server
    """

    # Instantiate the app ... __name__ indicates that the app
    # will be called "example_app"
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY")

    # No prefix example
    from example_app.route_one import bp as no_prefix_bp

    app.register_blueprint(no_prefix_bp)

    # URL prefix example
    from example_app.route_two import bp as with_prefix_bp

    app.register_blueprint(with_prefix_bp, url_prefix="/nba")

    ###

    # Tell the user that we're running
    logging.info(" === App Running ===")

    return app
