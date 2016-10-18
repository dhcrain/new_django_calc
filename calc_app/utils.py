

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def do_math(num1, operator, num2):
    if num2 == 0:
        return NaN
    else:
        option = {'+': add, '-': subtract, '/': divide, 'X': multiply}
        return option[operator](num1, num2)
