"""Interface for PostgreSQL database."""

from app.models import Item
from . import db


def save_item(name, timestamp, uitilization):
    """Save an item with a pool name, a timestamp, and a capacity utilization to the database."""
    item = Item(name=name, timestamp=timestamp, utilization=uitilization)
    db.session.add(item)
    db.session.commit()
    return item


def get_all_items():
    """Get all items from the database."""
    return Item.query.all()
