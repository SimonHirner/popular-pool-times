"""Data scraper for IKB website."""

import logging
import re
from math import nan
import requests
from bs4 import BeautifulSoup
from constants import (
    POOL_UTILIZATION_IDS,
    POOL_UTILIZATION_URL,
)

logger = logging.getLogger(__name__)


def scrape_pool_utilization_data():
    """Scrape pool utilization data."""
    logger.info("Scrape pool utilization data.")

    response = requests.get(POOL_UTILIZATION_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    data = []

    for name, utilization_id in POOL_UTILIZATION_IDS.items():
        text = soup.find(id=utilization_id).text.strip()

        match_utilization = re.search(r"\d+(?=\%)", text)
        if match_utilization:
            utilization = match_utilization.group(0)
        else:
            utilization = nan

        match_timestamp = re.search(r"\d{2}\.\d{2}\.\d{4}", text)
        if match_timestamp:
            timestamp = match_timestamp.group(0)
        else:
            timestamp = nan

        data.append(
            {
                "name": name,
                "timestamp": timestamp,
                "utilization": utilization,
            }
        )

    logger.debug("Pool utilization data was scraped: f{data}")

    return data
