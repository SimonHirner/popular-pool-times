"""Database models."""

from . import db

# pylint: disable=too-few-public-methods
class Item(db.Model):
    """Model for an item with a pool name, a timestamp, and a capacity utilization."""

    __tablename__ = "capacity_utilization"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    utilization = db.Column(db.Integer)

    def __init__(self, name, timestamp, utilization) -> None:
        self.name = name
        self.timestamp = timestamp
        self.utilization = utilization

    def __repr__(self):
        return f"Pool name: {self.name}, Timestamp: {self.timestamp}"
