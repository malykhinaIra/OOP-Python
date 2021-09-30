class Rectangle:

    def __init__(self, length=1, width=1):
        try:
           self.setRectangle(float(length), float(width))
        except:
            exit("Invalid input")

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    def getRectangle(self):
        return self.perimeter(),  self.area()

    def setRectangle(self, length, width):
        if width <= 0 or width >= 20 or length <= 0 or length >= 20:
            exit("Invalid input")
        else:
            self.length = length
            self.width = width


a = Rectangle(2.3, 5.0)
print(a.getRectangle())
