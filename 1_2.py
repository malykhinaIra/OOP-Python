import math


class Rational:

    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Numbers must be int values")
        else:
            divisor = math.gcd(numerator, denominator)
        if not denominator:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
            self.__numerator = numerator // divisor
            self.__denominator = denominator // divisor

    def fraction(self):
        return f'{self.__numerator}/{self.__denominator}'

    def calculation(self):
        return self.__numerator/self.__denominator


a = Rational(2, 10)
print(a.fraction())
print(a.calculation())