from folium import Map, Popup
from geo import Geopoint

# Get latitude and longitude values
locations=[[45.16667, 5.71667], [47.75, 7.33333], [48.85341, 2.3488], [43.3, -0.36667]]

# Folium Map instance
my_map = Map(location = [47.3, 5])

for loc in locations:
    # Creating a geopoint
    geopoint = Geopoint(loc[0], loc[1])

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