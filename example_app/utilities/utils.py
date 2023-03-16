#!/bin/python3
import random
from flask import flash

##########


def flash_a_message():
    """This function displays a random message on the screen"""

    options = [
        "Have a nice day!",
        "You're doing great!",
        "Everyone needs a friend like you!",
        "Make today great!",
    ]

    flash(random.choice(options))
