import math


class Rational:

    def __init__(self, numerator=1, denominator=1):
        try:
            divisor = math.gcd(int(numerator), int(denominator))
        except:
            print("Invalid input")
            exit(0)
        if denominator:
            self.__numerator = int(numerator) // divisor
            self.__denominator = int(denominator) // divisor
        else:
            print("Cannot divide by zero")
            exit(0)

    def printFraction(self):
        print(str(self.__numerator) + '/' + str(self.__denominator))

    def printFloat(self):
        print(self.__numerator/self.__denominator)


a = Rational(input("Numerator: "), input("Denominator: "))
a.printFraction()
a.printFloat()
