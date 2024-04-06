"""Entry point of the application."""

import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import DATABASE_URL, LOGGING_LEVEL, LOGGING_FORMAT


logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# pylint: disable=wrong-import-position
from app import routes, models
