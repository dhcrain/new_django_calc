

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
        result = option[operator](num1, num2)
        if result == int(result):
            return int(result)
        return round(result, 4)
