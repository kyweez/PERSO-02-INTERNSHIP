from folium import Map, Popup
from geo import Geopoint

# Get latitude and longitude values
latitude = 45.764043
longitude = 4.835659 

# Folium Map instance
my_map = Map(location = [latitude, longitude])

# Create a Geopoint instance
geopoint = Geopoint(latitude, longitude)
popup = Popup(str(geopoint.get_weather()))
popup.add_to(geopoint)
geopoint.add_to(my_map)

# Save the Map instance into HTML file
my_map.save("map.html")