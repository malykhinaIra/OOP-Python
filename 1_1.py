class Rectangle:

    def __init__(self, length=None, width=None):
        self.length = length
        self.width = width

    def __str__(self):
        return f'Perimeter = {self.perimeter()}, area = {self.area()}'

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if not (isinstance(length, float)):
            raise TypeError("Length has to be float value")
        if length <= 0 or length >= 20:
            raise ValueError("Length has to be larger than 0.0 and less than 20.0")
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not (isinstance(width, float)):
            raise TypeError("Width has to be float value")
        if width <= 0 or width >= 20:
            raise ValueError("Width has to be larger than 0.0 and less than 20.0")
        self.__width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2


a = Rectangle(7.0, 5.0)
print(a)
