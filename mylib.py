# mylib.py
import logging
import pandas as pd

def make_df_from_weather(forecast):
    logger = logging.getLogger(__name__)
    logger.info("Creating data frame from forecast JSON")
    return  pd.DataFrame.from_dict(forecast['forecast']['simpleforecast']['forecastday'])
