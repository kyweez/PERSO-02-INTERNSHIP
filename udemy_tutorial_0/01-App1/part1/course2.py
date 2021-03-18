from folium import Map

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
myMap.save("antipode_course2.html")

print("Latitude  :", antipode_latitude)
print("Longitude :", antipode_longitude)
print(myMap)