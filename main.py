"""
Author: Adam Frederick
Date: 2026-02-23
Project: Getting a weather forecast from NWS
"""
import requests
from pyld import jsonld
import forecast_map


#Harrison County ID = MSC047
base_url = 'https://api.weather.gov'
forecast = '/forecast'
alerts = '/alerts/active?area=MS'
lb_forecast = '/gridpoints/LIX/102,108/forecast'
test = '/zones/county/MSC047'
lat_long = '/points/30.375,-89.152'
complete_url = base_url + lb_forecast

response = requests.get(complete_url)
local_forecast = response.json()
# form_forcast = local_forecast.dumps()
#To get values of nested dictionary, you must stack [] searches.
data_props = local_forecast["properties"]
# data_props is a list type; periods in data_props is a dictionary with keys.
for i in data_props["periods"]:
    print(f'Forecast Period:{i["number"]}\nForecast:{i["detailedForecast"]}')

forecast_map.map_scrapper()

# print(type(local_forecast))
# for key in data_props["periods"].keys():
#     print(key)


# print(local_forecast["properties"]["periods"][0]["detailedForecast"])