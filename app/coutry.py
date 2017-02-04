from random import choice


class Country(object):
    country_dict = {
        'Sweden': {'min_lon': 10.958333, 'min_lat':	46.758333, 'max_lon':25, 'max_lat':	69.033333},
        'Norway': {'min_lon': 3.033333, 'min_lat':	56.15, 'max_lon':31.166667, 'max_lat':	71.181944},
        'Spain': {'min_lon': -18.166667, 'min_lat': 27.633333, 'max_lon': 4.333333, 'max_lat': 43.916667},
        'Taiwan': {'min_lon': 118.115255566105, 'min_lat': 21.733333, 'max_lon': 122.107778, 'max_lat': 26.389444},
        'Japan': {'min_lon': 122.933333, 'min_lat': 20.416667, 'max_lon': 154, 'max_lat': 45.520833},
        'South Africa': {'min_lon': 16.466667, 'min_lat': -34.833333, 'max_lon': 32.883333, 'max_lat': -22.133333},
    }

    @staticmethod
    def get_random_country_location():
        country = choice(list(Country.country_dict.keys()))
        return country, Country.country_dict[country]
