def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

def divide(a, b):
    if b==0: return 'Ошибка'
    return a / b

def mod(a, b):
    if b==0: return 'Ошибка'
    return a % b
import math

def power(a, b):
    return a ** b

def sqrt_num(a):
    if a<0: return 'Ошибка'
    return math.sqrt(a)
