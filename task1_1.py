class Rectangle:

    def __init__(self, length=1, width=1):
        self.set_length(length)
        self.set_width(width)

    def set_length(self, length):
        if not (isinstance(length, float)):
            raise TypeError("Length has to be float")
        if length <= 0 or length >= 20:
            raise ValueError("Length has to be larger than 0.0 and less than 20.0")
        else:
            self.length = length

    def set_width(self, width):
        if not (isinstance(width, float)):
            raise TypeError("Width has to be float")
        if width <= 0 or width >= 20:
            raise ValueError("Width has to be larger than 0.0 and less than 20.0")
        else:
            self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2


a = Rectangle(19.0, 5.0)
print(a.perimeter(), a.area())
a.set_width(5.0)
a.set_length(7.0)
print(a.perimeter(), a.area())

