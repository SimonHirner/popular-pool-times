"""Flask application and main module."""

import logging
from flask import Flask, render_template
from constants import LOGGING_FORMAT, LOGGING_LEVEL

logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT)
logger = logging.getLogger(__name__)

app = Flask(__name__)
logger.info("Application was started.")


@app.route("/")
def landing_page():
    """Landing page of application."""
    logger.debug("Landing page was called.")

    # Fetch data from the database
    # data = ""  # get_data_from_database()

    # Ceate visualization with Plotly
    # graph = ""  # create_visualization(data)

    info = "Popular Pool Times."

    return render_template("index.html", info=info)
