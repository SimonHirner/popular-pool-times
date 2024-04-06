"""Configuration of the application."""

import logging
import os

# Database
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Scraping
POOL_UTILIZATION_URL = "https://www.ikb.at/baeder/auslastung"
POOL_UTILIZATION_IDS = {
    "Hallenbad Amraser Straße": "cphInhalt_lblHBA_Bad2",
    "Hallenbad Olympisches Dorf": "cphInhalt_lblHBO_Bad2",
    "Hallenbad Höttinger Au": "cphInhalt_lblHBH_Bad2",
}

# Logging
LOGGING_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOGGING_LEVEL = logging.DEBUG
