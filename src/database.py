"""Interface for PostgreSQL database."""

import logging
import psycopg2
from constants import DATABASE_URI

logger = logging.getLogger(__name__)


def connect_to_database():
    """Connect to database."""
    logger.info("Connect to database.")

    conn = psycopg2.connect(database=DATABASE_URI)
    return conn


def save_to_database(data):
    """Save data to database."""
    logger.info("Save data to database: f{data}")

    conn = connect_to_database()
    cursor = conn.cursor()

    for item in data:
        cursor.execute(
            """
            INSERT INTO pools (name, timestamp, utilization)
            VALUES (%s, %s, %s)
            """,
            (item["name"], item["timestamp"], item["utilization"]),
        )

    conn.commit()
    conn.close()
