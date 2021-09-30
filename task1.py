class Rectangle:

    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    def getRectangle(self):
        return self.perimeter(),  self.area()

    def setRectangle(self, length, width):
        if width < 0 or width > 20 or type(width) is not float or length < 0 or length > 20 or type(length) is not float:
            print("Invalid input")
            exit(0)
        else:
            self.length = length
            self.width = width


a = Rectangle()
a.setRectangle(5.0, 3.0)
print(a.getRectangle())
