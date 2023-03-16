from flask import Blueprint

bp = Blueprint("route_one", __name__)

from example_app.route_one import routes
