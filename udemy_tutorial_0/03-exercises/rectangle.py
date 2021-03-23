class Rectangle:

    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height
    
    def distance_to_point(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2)**0.5