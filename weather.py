import pandas
import numpy as np
from datetime import datetime
import json
import pprint as pp
import requests
import logging

def main():
    """ Fetch the weather. """
    verbose = True
    logger = configure_logging(verbose)
    logger.info("Starting weather")
    gnv_forecast_url = 'http://api.wunderground.com/api/f77ce6503c744246/forecast10day/q/FL/Gainesville.json'
    logger.info("Fetching Gainesville weather.")
    gnv_forecast = requests.get(gnv_forecast_url)
    logger.debug("Response: {}".format(gnv_forecast.status_code))
    gnv_forecast_text = json.loads(gnv_forecast.text)
    pp.pprint(gnv_forecast_text)

def configure_logging(verbose):
    """Configure the logger."""
    # set up logging
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.DEBUG)
    # logging to file
    fh = logging.FileHandler('weather.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # logging to console
    ch = logging.StreamHandler()
    if verbose:
        ch.setLevel(logging.DEBUG)
    else:
        ch.setLevel(logging.WARNING)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger

if __name__ == '__main__':
    main()
