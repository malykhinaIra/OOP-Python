import math


class Rational:

    def __init__(self, numerator=1, denominator=1):
        divisor = math.gcd(numerator, denominator)
        self.__numerator = numerator // divisor
        self.__denominator = denominator // divisor

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise ValueError("Numerator must be int values")
        self.__numerator = numerator

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def numerator(self, denominator):
        if not isinstance(denominator, int):
            raise ValueError("denominator must be int values")
        if not denominator:
            raise ZeroDivisionError("Cannot divide by zero")
        self.__denominator = denominator

    def fraction(self):
        return f'{self.__numerator}/{self.__denominator}'

    def calculation(self):
        return self.__numerator/self.__denominator


a = Rational(2, 10)
print(a.fraction())
print(a.calculation())
