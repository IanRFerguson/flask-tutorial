from flask import Blueprint

bp = Blueprint("route_two", __name__)

from example_app.route_two import routes
