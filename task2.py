import math





class Rational:

    def __init__(self, numerator=1, denominator=1):
        try:
            gcd = math.gcd(numerator, denominator)
        except:
            print("Invalid input")
            exit(0)
        if denominator:
            self.__numerator = numerator // gcd
            self.__denominator = denominator // gcd
        else:
            print("Cannot divide by zero")
            exit(0)

    def printFraction(self):
        print(str(self.__numerator) + '/' + str(self.__denominator))

    def printFloat(self):
        print(self.__numerator/self.__denominator)


a = Rational(2, 8)
a.printFraction()
a.printFloat()
