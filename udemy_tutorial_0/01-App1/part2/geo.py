from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform
from folium import Map

class Geopoint:

    latitude_range = (-90, 90)
    longitude_range = (-180, 180)

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def closest_parallel(self):
        return round(self.latitude)
    
    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(lng=self.longitude, lat=self.latitude)
        time_now = datetime.now(timezone(timezone_string))
        return time_now

    def get_weather(self):
        weather = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", lat = self.latitude, lon = self.longitude)
        return weather.next_12h_simplified()

    @classmethod
    def random(cls):
        return cls(latitude = uniform(-90, 90),  longitude = uniform(-180, 180))

tokyo = Geopoint(latitude = 35.7, longitude = 139.7)
print(tokyo.closest_parallel())
print(tokyo.get_time())
print(tokyo.get_weather())

my_random_point = Map(location=[Geopoint.random().latitude, Geopoint.random().longitude]).save("random_point.html")

print(type(Geopoint.latitude_range))