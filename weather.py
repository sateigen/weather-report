import requests
# import json
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
        temp = conditions['temp_f']
        feels_like = conditions['feelslike_f']
        weather = conditions['weather']
        wind_dir = conditions['wind_dir']
        wind_speed = conditions['wind_mph']
        precip = conditions['precip_today_in']

        return "\tThe Local Forecast for {}\n\n\tCurrent Temperature: {}F\tFeels Like: {}F\n\tCurrent Condition: {}\n\tCurrent Wind: {}mph from the {}\n\tThere has been {}in of precipitation today\n".format(self.zipcode, temp, feels_like, weather, wind_speed, wind_dir, precip)

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


def welcome():
    print("Welcome to the Wunderground API Application")
    return input("Please enter a 5-digit zipcode.\n\t>> ")


def choose_view():
    print("""Here are your options of what to see.
          1. 10-day Forecast
          2. Current Weather""")
    return input("Please make a choice from above.\n\t>> ")


def main():
    zipcode = Weather(int(welcome()))
    zipcode.get_json()
    choice = int(choose_view())
    if choice == 1:
        for item in zipcode.get_forecast():
            print(item)
    elif choice == 2:
        print(zipcode.get_current_conditions())

if __name__ == '__main__':
    main()
