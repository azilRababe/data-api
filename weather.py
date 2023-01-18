# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://weather.lewagon.com/geo/1.0/direct?q="


def search_city(query):
    '''Look for a given city. If multiple options are returned, have the user choose between them.
       Return one city (or None)
    '''
    res= requests.get(BASE_URI+query).json()
    return res[0]


def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    URL=f'https://weather.lewagon.com/data/2.5/forecast?lat={lat}&lon={lon}'
    return (requests.get(URL).json()['list'][0]['weather'][0]['main'])



def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    # TODO: Display weather forecast for a given city
    forecast=weather_forecast(city['lat'],city['lon'])
    print(forecast)

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
