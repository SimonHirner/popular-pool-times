# Popular Pool Times for Innsbruck

## About the Project
This application shows how busy the swimming pools of the IKB in Innsbruck typically are during different times of the day. Unlike the [IKB website](https://www.ikb.at/baeder/auslastung), which only provides information about the current capacity utilization, this tool presents historical data on popular times. This offers visitors valuable information to plan their visits, avoid overcrowding, and ensuring a more enjoyable experience. Popular times are based on average capacity utilization over the last few weeks. The data for the capacity utilization is collected at regular intervals from the IKB website. Popularity for any given hour is shown relative to the typical peak popularity for the pool for the week. 

## Getting Started
### Prerequisites
* Linux Ubuntu
* Python version 3.10.12
* pip package installer

### Create a virtual environment
`python3 -m venv .venv`

### Activate the virtual environment
`source .venv/bin/activate`

### Install dependencies
`pip install -r requirements.txt`

### Run application on a Flask development server.
`flask run`

### Run application on a Gunicorn server
`gunicorn app:app`

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.