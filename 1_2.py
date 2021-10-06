import math


class Rational:

    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Numbers must be int values")
        else:
            divisor = math.gcd(numerator, denominator)
        if denominator:
            self.__numerator = numerator // divisor
            self.__denominator = denominator // divisor
        else:
            raise ZeroDivisionError("Cannot divide by zero")

    def fraction(self):
        return f'{self.__numerator}/{self.__denominator}'

    def calculation(self):
        return self.__numerator/self.__denominator


a = Rational(2, 10)
print(a.fraction())
print(a.calculation())