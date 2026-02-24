"""
Author: Adam Frederick
Date: 2026-02-23
Project: Getting a weather forecast from NWS
"""
import requests
import forecast_extract
import forecast_map


forecast_extract.extract_forecast()
forecast_map.map_scrapper()

