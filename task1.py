class Rectangle:

    def __init__(self, length=1, width=1):
        try:
           self.setRectangle(float(length), float(width))
        except:
            exit(0)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    def getRectangle(self):
        return self.perimeter(),  self.area()

    def setRectangle(self, length, width):
        if width <= 0 or width > 20 or length <= 0 or length > 20:
            print("Invalid input")
            exit(0)
        else:
            self.length = length
            self.width = width


a = Rectangle(input("Length: "), input("Width: "))
print(a.getRectangle())
