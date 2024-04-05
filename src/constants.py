"""Constants of the application."""

import logging

# Database
DATABASE_URI = "postgres://user:password@host:port/database_name"

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
