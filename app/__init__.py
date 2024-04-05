"""Entry point of the application."""

import logging
from flask import Flask
from app.config import LOGGING_LEVEL, LOGGING_FORMAT

logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT)

app = Flask(__name__)

# pylint: disable=wrong-import-position
from app import routes, models
