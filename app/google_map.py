import requests
from random import uniform
from app import db
from models import Country
from sqlalchemy.sql.expression import func
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


class GoogleMap(object):
    @staticmethod
    def get_street_view():
        counter = 0
        while True:
            if counter % 100 == 0:
                random_countries = db.session.query(Country).order_by(func.random()).limit(4)
                random_country = random_countries[0]
            latitude = uniform(random_country.min_lat, random_country.max_lat)
            longitude = uniform(random_country.min_lon, random_country.max_lon)
            coordinate = "{0:.7f}".format(round(latitude, 7)) + "," + "{0:.7f}".format(round(longitude, 7))
            url = "http://maps.google.com/cbk?output=json&hl=en&ll=" + coordinate + "&radius=10&cb_client=maps_sv&v=4"
            print url
            result = requests.get(url)
            print result.json()
            if (len(result.json())) != 0:
                break
            else:
                counter += 1
        pic_url = "https://maps.googleapis.com/maps/api/streetview?size=600x600&location=" + coordinate
        pic_url += "&key=" + GOOGLE_API_KEY
        return pic_url, random_countries

