import unittest
import math
from math import factorial

class Calculator(object):
    @staticmethod
    def addition(x, y):
        sum = x + y
        return sum

    @staticmethod
    def divide(x, y):
        if y == 0:
            return 'NaN'
        else:
            divd = float(x) / float(y)
            return divd

    @staticmethod
    def exponent(x, y):
        exp = x ** y
        return exp

    @staticmethod
    def multiply(x, y):
        mult = x * y
        return mult

    @staticmethod
    def subtraction(x, y):
        sub = x - y
        return sub

    @staticmethod
    def nth_root(x, y):
        nroot = (x ** (1.0 / y))
        return nroot

    @staticmethod
    def fahrenheit_to_celsius(x):
        cel = float((x - 32.0) * float(5.0 / 9.0))
        return cel

    @staticmethod
    def factorial(x):
        num = 1
        while x >= 1:
            num = num * x
            x = x - 1
        return num

        # print factorial(x)
    @staticmethod
    def calculate_combinations(x, y):
        # from math import factorial
        return factorial(x) // factorial(y) // factorial(x - y)

        # print calculate_combinations(x, y)

    @staticmethod
    def square_root(x):
        sqr = math.sqrt(x)
        return sqr


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()


    def test_factorial(self):
        result = factorial(5)
        self.assertEqual(120, result)
        result = factorial(6)
        self.assertEqual(720, result)

    def test_calculator_addition(self):
        result = self.calc.addition(2, 2)
        self.assertEqual(4, result)
        result = self.calc.addition(2,4)
        self.assertEqual(6, result)
        result = self.calc.addition(2, -2)
        self.assertEqual(0, result)

    def test_calculator_subtraction(self):
        result = self.calc.subtraction(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtraction(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtraction(2, -4)
        self.assertEqual(6, result)



    def test_calculator_multiply(self):
        result = self.calc.multiply(2, 2)
        self.assertEqual(4, result)
        result = self.calc.multiply(2,4)
        self.assertEqual(8, result)
        result = self.calc.multiply(2, -2)
        self.assertEqual(-4, result)
        result = self.calc.multiply(2, 0)
        self.assertEqual(0, result)
        result = self.calc.multiply(2, 0)
        self.assertEqual(0, result)

    # adding divide to my calculator
    def test_calculator_divide(self):
        result = self.calc.divide(2, 2)
        self.assertEqual(1, result)
        result = self.calc.divide(4,2)
        self.assertEqual(2, result)
        result = self.calc.divide(2, -2)
        self.assertEqual(-1, result)
        result = self.calc.divide(2, 4)
        self.assertEqual(0.5, result)
        result = self.calc.divide(2, 0)
        self.assertEqual('NaN', result)


    # adding exponent to my calculator
    def test_calculator_exponent(self):
        result = self.calc.exponent(2, 2)
        self.assertEqual(4, result)
        result = self.calc.exponent(2,4)
        self.assertEqual(16, result)
        result = self.calc.exponent(2, -2)
        self.assertEqual(0.25, result)
        result = self.calc.exponent(2, 0)
        self.assertEqual(1, result)

    def test_fahrenheit_to_celsius(self):
        result = round(self.calc.fahrenheit_to_celsius(99), 5)
        self.assertEqual(37.22222, result)
        result = round(self. calc.fahrenheit_to_celsius(999),5)
        self.assertEqual(537.22222, result)

    def test_combination(self):
        result = self.calc.calculate_combinations(10, 2)
        self.assertEqual(45, result)
        result = self.calc.calculate_combinations(8, 3)
        self.assertEqual(56, result)

    def test_square_root(self):
        result = self.calc.square_root(16)
        self.assertEqual(4, result)
        result = self.calc.square_root(81)
        self.assertEqual(9, result)

    def test_nth_root(self):
        result = self.calc.nth_root(8, 3)
        self.assertEqual(2, result)
        result = self.calc.nth_root(27, 3)
        self.assertEqual(3, result)

if __name__ == '__main__':
    unittest.main()
