#!/bin/python3
from flask import render_template
from dotenv import load_dotenv
import random
import logging

from example_app import env_path
from example_app.route_two import bp

load_dotenv(env_path)
logging.basicConfig(level=logging.INFO)

##########


@bp.route("/90s_legends", methods=["GET", "POST"])
def another_good_example():
    """
    90S LEGENDS ROUTE

    When this route is registered by Flask we're going to attach a URL prefix to it.
    Run the app and note the URL when you hit this route, you should see a leading "/nba"
    """

    logging.info("Hit the 90s legends route!")

    # Dictionary of values for each NBA player
    superstars = {
        "Patrick Ewing": {
            "image_source": "https://www.si.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cg_xy_center%2Cq_auto:good%2Cw_1200%2Cx_2189%2Cy_649/MTg5NzA2ODExMTE1MzE2NDIx/usatsi_8742383.jpg",
            "team": "New York Knicks",
        },
        "Michael Jordan": {
            "image_source": "https://www.nbcsports.com/sites/rsnunited/files/styles/responsive_background_mobile/public/archive/assets_media_gallery/chicago/2020/05/21/jordan_thumb-1.jpg",
            "team": "Chicago Bulls",
        },
        "Charles Barkley": {
            "image_source": "https://www.golfdigest.com/content/dam/images/golfdigest/fullset/2021/1/CharlesBarkley_PhoenixSuns.jpg",
            "team": "Phoenix Suns",
        },
        "Penny Hardaway": {
            "image_source": "https://cdn.vox-cdn.com/thumbor/2Fisw2vKlnhqjb5BSZ1Ns15G650=/0x0:2430x3600/1200x800/filters:focal(974x1158:1362x1546)/cdn.vox-cdn.com/uploads/chorus_image/image/69511386/903568036.0.jpg",
            "team": "Orlando Magic",
        },
        "Kareem Abdul-Jabar": {
            "image_source": "https://i.ebayimg.com/images/g/4vgAAOSwv7BdFDVb/s-l500.jpg",
            "team": "Los Angeles Lakers",
        },
    }

    # Randomly pick a key from the dictionary
    key = random.choice([x for x in superstars.keys()])

    # Access the values for the selected player
    star = superstars[key]

    """
    Here we're going to pass values to the HTML, which we will render with Jinja

    Take a look at "templates/route_two.html" and look at how the logic is folded
    in with {{ }} braces
    """

    logging.info(f"Rendering {key}'s information...")

    return render_template(
        "route_two.html",
        image=star["image_source"],
        team=star["team"],
        full_name=key,
        first_name=key.split(" ")[0],
    )
