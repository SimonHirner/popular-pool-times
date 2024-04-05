"""Web routes of Flask application."""

from flask import render_template
from app import app


@app.route("/")
def index():
    """Landing page of application."""
    app.logger.debug("Landing page was called.")

    # Fetch data from the database
    # data = ""  # get_data_from_database()

    # Ceate visualization with Plotly
    # graph = ""  # create_visualization(data)

    info = "Popular Pool Times."

    return render_template("index.html", info=info)
