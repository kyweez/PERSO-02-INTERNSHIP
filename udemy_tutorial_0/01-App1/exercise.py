wall_area = 200.5
buckets = wall_area * 2.5

white_price = 1.99
color_price = 2.19

color = "red"

if color == "white":
    total_price = buckets * white_price
else:
    total_price = buckets * color_price

print(total_price)