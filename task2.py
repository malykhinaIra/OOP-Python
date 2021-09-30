import math


class Rational:

    def __init__(self, numerator=1, denominator=1):
        try:
            divisor = math.gcd(int(numerator), int(denominator))
        except:
            exit("Invalid input")
        if denominator:
            self.__numerator = int(numerator) // divisor
            self.__denominator = int(denominator) // divisor
        else:
            exit("Cannot divide by zero")

    def fraction(self):
        return str(self.__numerator) + '/' + str(self.__denominator)

    def calculation(self):
        return self.__numerator/self.__denominator


a = Rational(2, 10)
print(a.fraction())
print(a.calculation())