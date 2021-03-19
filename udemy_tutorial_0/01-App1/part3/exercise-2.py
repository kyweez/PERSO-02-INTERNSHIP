class House:

    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        return self.wall_area * 2.5
        

class Paint:

    def __init__(self, buckets, color): 
        self.color = color
        self.buckets = buckets

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19

my_house = House(1500)
paint_needed_for_my_house = my_house.paint_needed()
red_paint_needed = Paint(paint_needed_for_my_house, "red")
price = red_paint_needed.total_price()
message = f"The total price is {price}"
print(message)