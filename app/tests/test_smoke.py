"""Smoke tests for Flask application."""

import pytest
from app import app


@pytest.fixture
def client():
    """Test fixture."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    """Smoke test for index page."""
    response = client.get("/")
    assert response.status_code == 200


def test_nonexistant_page(client):
    """Smoke test for index page."""
    response = client.get("/nonexistant")
    assert response.status_code == 404
