# -*- coding: utf-8 -*-
import numpy
"""
This code file contains the multiple procedures to perform basic
mathematical calculations such as add, subtract, multiply and divide.
Note: Divide2 function is particularly developed to produce custom
error on division by zero error.
"""

def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multipy Function"""
    return x * y

# with numpy
def divide(x, y):
    """Divide Function"""
    return numpy.float64(x) / y

#without numpy
def divide2(x, y):
    """Divide Function"""        
    if y == 0:
        raise ValueError('Division by zero is not permitted. Its always supposed to return infinite value')
    else:
        return x / y

def printResult(x):
    if x == float("inf"):
        print ("Resul is infinite!")
    else:
        print ("Result equals " + str(x))

if __name__ == '__main__':
    #test add method
    x = add(5, 2)
    printResult(x)
    #test subtract method
    x = subtract(5, 2)
    printResult(x)
    #test multiplication
    x = multiply(5, 2)
    printResult(x)
    #test division method
    x = divide(5, 2)
    printResult(x)
    #test valueError on division by zero
    #x = divide2(5, 0)
    #printResult(x)
    #x = divide2(10, 0)