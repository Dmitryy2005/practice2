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
import math

def sin_deg(a):
    return math.sin(math.radians(a))

def cos_deg(a):
    return math.cos(math.radians(a))
