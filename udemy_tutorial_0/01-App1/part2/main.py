from folium import Map
from geo import Geopoint
latitude = -45.1667
longitude = -174.2833

antipode_latitude = latitude * -1

if longitude < 0:
    antipode_longitude = longitude + 180
elif longitude == 0:
    antipode_longitude = 180
elif longitude > 180:
    antipode_longitude = "Invalid longitude"
else:
    antipode_longitude = longitude -180

location = [antipode_latitude, antipode_longitude]
myMap = Map(location)
myMap.save("antipode.html")

myPoint = Geopoint(41.2, 4.1)
myPoint.closest_parallel()

print("Latitude  :", antipode_latitude)
print("Longitude :", antipode_longitude)
print(myMap)
print(myPoint.closest_parallel())