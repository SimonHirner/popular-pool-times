"""Data scraper for IKB website."""

import datetime
import re
from math import nan
import requests
from bs4 import BeautifulSoup
from app.config import (
    POOL_UTILIZATION_IDS,
    POOL_UTILIZATION_URL,
)
from app import app


def scrape_pool_utilization_data():
    """Scrape pool utilization data."""
    app.logger.info("Scrape pool utilization data.")

    response = requests.get(POOL_UTILIZATION_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    data = []

    for name, utilization_id in POOL_UTILIZATION_IDS.items():
        text = soup.find(id=utilization_id).text.strip()

        match_utilization = re.search(r"\d+(?=\%)", text)
        if match_utilization:
            utilization_string = match_utilization.group(0)
            utilization = int(utilization_string)
        else:
            utilization = nan

        match_timestamp = re.search(r"\d+\.\d+\.\d+\s+\d+:\d+", text)
        if match_timestamp:
            timestamp_string = match_timestamp.group(0)
            timestamp = datetime.datetime.strptime(timestamp_string, "%d.%m.%Y %H:%M")
        else:
            timestamp = nan

        data.append(
            {
                "name": name,
                "timestamp": timestamp,
                "utilization": utilization,
            }
        )

    app.logger.debug("Pool utilization data was scraped: f{data}")

    return data
