import pandas
import numpy as np
from datetime import datetime
import json
import pprint as pp
import requests
import logging

def main():
    """ Fetch the weather. """
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='weather.log', level=logging.DEBUG)
    logging.info("Starting weather")
    gnv_forecast_url = 'http://api.wunderground.com/api/f77ce6503c744246/forecast10day/q/FL/Gainesville.json'
    logging.info("Fetching Gainesville weather.")
    gnv_forecast = requests.get(gnv_forecast_url)
    logging.debug("Response: {}".format(gnv_forecast.status_code))
    gnv_forecast_text = json.loads(gnv_forecast.text)
    #pp.pprint(gnv_forecast_text)



if __name__ == '__main__':
    main()
