# Popular Pool Times for Innsbruck
**Visit the application: [Popular Pool Times](https://popular-pool-times-bfbb4c6e23b9.herokuapp.com/)**

## About the Project
This application shows how busy the swimming pools of the IKB in Innsbruck typically are during different times of the day. Unlike the [IKB website](https://www.ikb.at/baeder/auslastung), which only provides information about the current capacity utilization, this tool presents historical data on popular times. This offers visitors valuable information to plan their visits, avoid overcrowding, and ensuring a more enjoyable experience. Popular times are based on average capacity utilization over the last few weeks. Popularity for any given hour is shown relative to the typical peak popularity for the pool for the week. The data for the capacity utilization is collected at regular intervals from the IKB website. Based on the terms of use, scraping the IKB website for personal, non-commercial use is permissible as long as the content is not altered and the source is properly attributed. The scraping involves a small amount of data and requests, which reduces the likelihood of causing disruption or strain on the website's servers.

## Data Source
The source of the data is Innsbrucker Kommunalbetriebe AG. The capacity utilization of the pools is collected from the [IKB website](https://www.ikb.at/baeder/auslastung).

## Disclaimer
I am not affiliated with Innsbrucker Kommunalbetriebe AG. The use of their content in this personal project does not imply any endorsement or association with the company. This project is solely for personal, non-commercial purposes.

## Architecture
The application consits of three main components:
* Web scraper for collecting the pool capacity utilization data.
* PostgreSQL database to store the collected data.
* Flask web application for the visualization of the collected data.
    * SQLAlchemy library for efficient relational database access
    * Beautiful Soup library for web scraping

## Getting Started

### Prerequisites
* Linux Ubuntu
* Python version 3.10.12
* pip package installer
* PostgreSQL database

### Installation

Create a virtual environment.

`python3 -m venv .venv`

Activate the virtual environment.

`source .venv/bin/activate`

Install dependencies.

`pip install -r requirements.txt`

### Usage

Set environment variable for your local PostgreSQL database.

`export DATABASE_URL="postgresql:///pool_db"`

Run application on a Flask development server.

`flask run`

Run application on a Gunicorn server.

`gunicorn app:app`

### Testing

`pytest`

### Linting

`pylint app/.`

## Database Migration
Database migration is necessary for changing the database schemas without any data loss.

Setting up Flask-Migrate.

`flask db init`

Create migration.

`flask db migrate -m "initial migration"`

Perform an upgrade.

`flask db upgrade`

## Deployment

The application is deployed in a Heroku Dyno with a PostgreSQL database.

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.
