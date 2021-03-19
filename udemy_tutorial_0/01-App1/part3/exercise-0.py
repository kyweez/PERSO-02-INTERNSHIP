class Paint:

    def __init__(self, buckets, color): # Or get house area and height
        self.color = color
        self.buckets = buckets

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19

class DiscountedPaint(Paint):

    def __init__(self, buckets, color):
        super().__init__(buckets, color)
        self.buckets = buckets
        self.color = color

    def discounted_price(self, discount_percentage):
        price_before_discount = self.total_price()
        discount = price_before_discount * discount_percentage / 100
        return price_before_discount - discount