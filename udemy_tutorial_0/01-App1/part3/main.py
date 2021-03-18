from folium import Map, Marker

# Get latitude and longitude values
latitude = 45.183941
longitude = 5.705446


# Folium Map instance
my_map = Map(location = [latitude, longitude])

# Create a Marker instance
grenoble = Marker(location = [45.183941, 5.705446], popup="Hi there")
grenoble.add_to(my_map)

# Save the Map instance into HTML file
my_map.save("map.html")