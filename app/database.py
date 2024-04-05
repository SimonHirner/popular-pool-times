"""Interface for PostgreSQL database."""

import psycopg2
from app.config import DATABASE_URI
from app import app


def connect_to_database():
    """Connect to database."""
    app.logger.info("Connect to database.")

    conn = psycopg2.connect(database=DATABASE_URI)
    return conn


def save_to_database(data):
    """Save data to database."""
    app.logger.info("Save data to database: f{data}")

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
