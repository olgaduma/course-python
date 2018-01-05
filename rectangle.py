class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def rectangle_area(self):
        return self.length*self.width
    def rectangle_perimeter(self):
        return (self.length+self.width)*2

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())
print(newRectangle.rectangle_perimeter())