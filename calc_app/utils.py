

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
        str_num1 = str(num1)
        str_num2 = str(num2)
        if str_num1[:2:-1] == '' and str_num2[:2:-1] == '':
            return int(result)
        return round(result, 4)
