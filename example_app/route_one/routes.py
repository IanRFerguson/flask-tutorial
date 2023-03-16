#!/bin/python3
from flask import render_template, redirect, url_for, request
from dotenv import load_dotenv
import random
import logging

from example_app import env_path
from example_app.route_one import bp
from example_app.utilities.utils import flash_a_message

load_dotenv(env_path)
logging.basicConfig(level=logging.INFO)

##########


@bp.route("/", methods=["GET", "POST"])
@bp.route("/home_route", methods=["GET", "POST"])
def index():
    """
    LANDING PAGE

    This route renders the index.html file, which we're using
    as landing page
    """

    logging.info("Hit the landing route!")

    """
    When we send a POST request, we're telling the Flask app that we
    want a function to trigger. In this case we want to trigger the
    flash_a_message() function and then redirect back to the index (the same
    route that we're writing this code in)

    Run the app and watch the output - you'll see a POST request followed immediately
    by a GET request for 
    """

    if request.method == "POST":
        flash_a_message()

        name = random.choice(["Patrick", "Jeremy", "Robb", "Leo", "Joan", "Jose"])

        return redirect(url_for("route_one.interactive_route", name=name))

    return render_template("index.html")


@bp.route("/state_flags", methods=["GET", "POST"])
def example_route():

    logging.info("Hit the state flag route!")

    state_flags = {
        "California": "https://cdn.britannica.com/46/7046-004-BB1F8E32/state-flag-Bear-Flag-California-red-star-July-9-1846.jpg",
        "New York": "https://cdn.britannica.com/14/3014-004-BD154711/flag-New-York-color-uniforms-facings-American-1909.jpg",
        "Virginia": "https://cdn.britannica.com/40/4940-004-63FAF073/Flag-Virginia.jpg",
        "North Carolina": "https://cdn.britannica.com/85/3085-004-29C93A89/design-independence-Union-flag-convention-state-North-April-12-1776.jpg",
        "Pennsylvania": "https://cdn.britannica.com/29/3429-004-4A64B1C5/Pennsylvania-state-flag-William-Penn-blue-coat-1777.jpg",
    }

    state = random.choice([x for x in state_flags.keys()])

    return render_template(
        "route_one.html", state_name=state, flag_image=state_flags[state]
    )


@bp.route("/interactive/<name>", methods=["GET", "POST"])
def interactive_route(name: str):
    return render_template("interactive.html", name=name)
