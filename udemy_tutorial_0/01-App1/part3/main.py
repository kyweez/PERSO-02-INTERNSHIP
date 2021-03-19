from folium import Map, Popup
from geo import Geopoint

# Get latitude and longitude values
latitude = 45.766043
longitude = 4.860659 

# Folium Map instance
my_map = Map(location = [latitude, longitude])

# Creating a geopoint
geopoint = Geopoint(latitude, longitude)

# Getting the geopoint forecast
forecast = geopoint.get_weather()

# Generating the popup content
popup_content = f"""
{forecast[0][0][-8:-6]}h / {round(((forecast[0][1]-32) * 5/9), 1)}°C <img src="http://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png" width="35">
<hr style="margin:1px">
{forecast[1][0][-8:-6]}h / {round(((forecast[1][1]-32) * 5/9), 1)}°C <img src="http://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png" width="35">
<hr style="margin:1px">
{forecast[2][0][-8:-6]}h / {round(((forecast[2][1]-32) * 5/9), 1)}°C <img src="http://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png" width="35">
<hr style="margin:1px">
{forecast[3][0][-8:-6]}h / {round(((forecast[3][1]-32) * 5/9), 1)}°C <img src="http://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png" width="35">
"""

# Creating and adding popup to geopoint
popup = Popup(popup_content, max_width=400)
popup.add_to(geopoint)

# Adding geopoint to the map
geopoint.add_to(my_map)

# Save the Map instance into HTML file
my_map.save("map.html")