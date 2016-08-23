import requests
import json


class Weather():
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.json_file = None # dict_keys(['moon_phase', 'query_zone', 'response'])

    # http://api.wunderground.com/api/c388c14844aa76bb/features/settings/q/query.format
    def get_json(self):
        request = requests.get('http://api.wunderground.com/api/c388c14844aa76bb/alerts/astronomy/conditions/currenthurricane/forecast10day/q/{}.json'.format(self.zipcode))
        json_string = request.json()
        # with open('data/{}.json'.format(self.zipcode), 'w') as f:
        #     json.dump(json_string, f)
        self.json_file = json_string

    def get_current_conditions(self):
        conditions = self.json_file['current_observation']

    def get_forecast(self):
        forecast = self.json_file['forecast']

    def get_rise_set(self):
        sun = self.json_file['sun_phase']

    def get_alerts(self):
        alerts = self.json_file['alerts']

    def get_hurricanes(self):
        hurricanes = self.json_file['currenthurricane']

chester = Weather(23831)
chester.get_json()
print(chester.json_file)
