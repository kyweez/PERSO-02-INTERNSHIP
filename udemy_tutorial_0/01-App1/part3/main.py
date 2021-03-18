from folium import Map, Marker
from folium.map import Popup
from geo import Geopoint

# Get latitude and longitude values
latitude = 45.183941
longitude = 6.705446

# Folium Map instance
my_map = Map(location = [latitude, longitude])

# Create a Geopoint instance
geopoint = Geopoint(latitude, longitude)
geopoint.add_to(my_map)

# Create a Marker instance
grenoble = Marker(location = [45.183941, 5.705446], popup="Hi there")
grenoble.add_to(my_map)

# Save the Map instance into HTML file
my_map.save("map.html")