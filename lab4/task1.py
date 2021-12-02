import math


class Rational:

    def __init__(self, numerator=1, denominator=1):
        self.divisor = math.gcd(numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Invalid type")
        if isinstance(other, int):
            other = Rational(other)
        res_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        res_denominator = other.denominator * self.denominator
        return f'{res_numerator // math.gcd(res_numerator, res_denominator)}' \
               f'/{res_denominator // math.gcd(res_numerator, res_denominator)}'

    def __iadd__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Invalid type")
        if isinstance(other, int):
            other = Rational(other)
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator = other.denominator * self.denominator
        return self

    def __sub__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Invalid type")
        if isinstance(other, int):
            other = Rational(other)
        res_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        res_denominator = other.denominator * self.denominator
        return f'{res_numerator // math.gcd(res_numerator, res_denominator)}' \
               f'/{res_denominator // math.gcd(res_numerator, res_denominator)}'

    def __isub__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Invalid type")
        if isinstance(other, int):
            other = Rational(other)
        self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        self.denominator = other.denominator * self.denominator
        return self

    def __mul__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Invalid type")
        if isinstance(other, int):
            other = Rational(other)
        res_numerator = self.numerator * other.numerator
        res_denominator = other.denominator * self.denominator
        return f'{res_numerator // math.gcd(res_numerator, res_denominator)}' \
               f'/{res_denominator // math.gcd(res_numerator, res_denominator)}'

    def __imul__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Invalid type")
        if isinstance(other, int):
            other = Rational(other)
        self.numerator = self.numerator * other.numerator
        self.denominator = self.denominator * other.denominator
        return self

    def __truediv__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Invalid type")
        if isinstance(other, int):
            other = Rational(other)
        res_numerator = self.numerator * other.denominator
        res_denominator = self.denominator * other.numerator
        return f'{res_numerator // math.gcd(res_numerator, res_denominator)}' \
               f'/{res_denominator // math.gcd(res_numerator, res_denominator)}'

    def __itruediv__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Invalid type")
        if isinstance(other, int):
            other = Rational(other)
        self.numerator = self.numerator * other.denominator
        self.denominator = self.denominator * other.numerator
        return self

    def __lt__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Invalid type")
        if isinstance(other, int):
            other = Rational(other)
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Invalid type")
        if isinstance(other, int):
            other = Rational(other)
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Invalid type")
        if isinstance(other, int):
            other = Rational(other)
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Invalid type")
        if isinstance(other, int):
            other = Rational(other)
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __eq__(self, other):
        if not isinstance(other, (int, Rational)):
            raise TypeError("Invalid type")
        if isinstance(other, int):
            other = Rational(other)
        return self.numerator == other.numerator and self.denominator == other.denominator

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise ValueError("Numerator must be int value")
        self.__numerator = numerator // self.divisor

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator):
        if not isinstance(denominator, int):
            raise ValueError("Denominator must be int value")
        if not denominator:
            raise ZeroDivisionError("Cannot divide by zero")
        self.__denominator = denominator // self.divisor

    def fraction(self):
        return f'{self.numerator}/{self.denominator}'

    def calculation(self):
        return self.numerator / self.denominator


a = Rational(1, 2)
b = Rational(6, 10)

print(a.fraction())
print(a + b)
print(a - 1)
print(a * 2)
print(a == 2)
a -= 1
print(a.fraction())
