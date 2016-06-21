import unittest
import math #importing the required maths libraries
import numpy as np
from math import factorial
operation = int(raw_input("Please select a Function: \n 1: Addition \n 2: Subtraction \n 3: Multiplication \n 4: Division \n 5: Exponents \n 6: Fahrenheit-Celcius \n 7: Factorials \n 8: Square Root \n 9: Combination \n 10: nth root\n:"))

x = int(raw_input('Please enter your first number: '))
if(operation ==1  or operation == 3 or operation == 3 or operation == 4 or operation == 5 or operation == 9 or operation == 10): #as some functions only require the input of 1 number
    y = int(raw_input('Please enter your second number: '))
#Creating a class containing 10 functions
class Calculator(object):
    @staticmethod
    #With staticmethods, neither self (the object instance)
    # nor  cls (the class) is implicitly passed as the first argument. They behave
    # like plain functions except that you can call them from an instance or the class:
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
        nroot = (x ** (1.0/y))
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


    @staticmethod
    def calculate_combinations(x, y):

        return factorial(x) // factorial(y) // factorial(x - y)



    @staticmethod
    def square_root(x):
        sqr = math.sqrt(x)
        return sqr



if (operation == 1):
    output1 = Calculator.addition(x,y)
    print(output1)
elif(operation == 2):
    output2 = Calculator.subtraction(x,y)
    print(output2)
elif(operation == 3):
    output3 = Calculator.multiply(x,y)
    print(output3)
elif(operation == 4):
   output4 = Calculator.divide(x,y)
   print(output4)
elif(operation == 5):
    output5 = Calculator.exponent(x,y)
    print(output5)
elif(operation == 6):
    output6 = Calculator.fahrenheit_to_celsius(x)
    print(output6)
elif(operation == 7):
    output7 = Calculator.factorial(x)
    print(output7)
elif(operation == 8):
    output8 = Calculator.square_root(x)
    print(output8)
elif(operation == 9):
    output9 = Calculator.calculate_combinations(x,y)
    print(output9)
elif(operation == 10):
    output10 = Calculator.nth_root(x,y)
    print(output10)
			


