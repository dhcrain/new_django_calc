
def int_or_float(num):
    if num == int(num):
        num = int(num)
    return num


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def do_math(num1, operator, num2):
    if num2 == 0 and operator == '/':
        return "Can't Divided By Zero"
    else:
        option = {'+': add, '-': subtract, '/': divide, 'X': multiply}
        result = int_or_float(option[operator](num1, num2))
        return round(result, 4)
