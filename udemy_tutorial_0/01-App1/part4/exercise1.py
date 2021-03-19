class House:
    paint_per_unit = 2.5

    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        return self.wall_area * self.paint_per_unit


class Paint:

    def __init__(self, buckets, color):
        self.color = color
        self.buckets = buckets

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19

# The colors and wall areas of the customer's houses
houses = [['white', 325.6], ['yellow', 410], ['cyan', 210.2]]

for color, area in houses:
    house = House(area)
    paint_amount = house.paint_needed()
    paint = Paint(buckets=paint_amount, color=color)
    print(paint.total_price()) # Print the total price of paint needed to paint the house