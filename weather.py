import pandas as pd
import numpy as np
from datetime import datetime
import json
import pprint as pp
import requests
import logging
import sys
import mylib


def main():
    """ Fetch the weather. """
    #logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='weather.log', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info("Starting weather")

    logger.info("Reading in config from file")
    try:
        f = open('config.txt')
        s = f.readline()
    except Exception:
        logger.error("Unable to read file.", exc_info = True)
    gnv_forecast_url = 'http://api.wunderground.com/api/f77ce6503c744246/forecast10day/q/FL/Gainesville.json'
    logger.info("Fetching Gainesville weather.")
    gnv_forecast = requests.get(gnv_forecast_url)
    logger.debug("Response: {}".format(gnv_forecast.status_code))
    gnv_forecast_text = json.loads(gnv_forecast.text)
    #pp.pprint(gnv_forecast_text)

    df = mylib.make_df_from_weather(gnv_forecast_text)
    #.transpose()
    #time = np.array(df[''])
    #print(df)


if __name__ == '__main__':
    main()
