import requests
import json
from secrets import API_KEY


class Weather():
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.json_file = None # dict_keys(['moon_phase', 'query_zone', 'response'])

    # http://api.wunderground.com/api/c388c14844aa76bb/features/settings/q/query.format
    def get_json(self):
        request = requests.get('http://api.wunderground.com/api/{}/alerts/astronomy/conditions/currenthurricane/forecast10day/q/{}.json'.format(API_KEY, self.zipcode))
        json_string = request.json()
        # with open('data/{}.json'.format(self.zipcode), 'w') as f:
        #     json.dump(json_string, f)
        self.json_file = json_string

    def get_current_conditions(self):
        conditions = self.json_file['current_observation']

    def get_forecast(self):
        ten_day = []
        forecast = self.json_file['forecast']
        for idx, item in enumerate(forecast['simpleforecast']['forecastday']):
            condition = item['conditions']
            temp = item['high']['fahrenheit']
            date_dict = forecast['simpleforecast']['forecastday'][idx]['date']
            day = date_dict['weekday']
            month = date_dict['monthname']
            date = date_dict['day']
            ten_day.append("\tForecast for {}, {} {}\n\tCondition: {}\n\tTemperature(F): {}\n".format(day, month, date, condition, temp))
        return ten_day

    def get_rise_set(self):
        sun = self.json_file['sun_phase']

    def get_alerts(self):
        alerts = self.json_file['alerts']

    def get_hurricanes(self):
        hurricanes = self.json_file['currenthurricane']

# chester = Weather(23831)
# chester.get_json()
# for item in chester.get_forecast():
#     print(item)
#     # print(chester.get_forecast())


def welcome():
    print("Welcome to the Wunderground API Application")
    return input("Please enter a 5-digit zipcode.\n\t>> ")


def choose_view():
    print("""Here are your options of what to see.
          1. 10-day Forecast""")
    return input("Please make a choice from above.\n\t>> ")


def main():
    zipcode = Weather(int(welcome()))
    zipcode.get_json()
    if int(choose_view()) == 1:
        for item in zipcode.get_forecast():
            print(item)

if __name__ == '__main__':
    main()
