import math

# Power functions

def identity(x):
    return x

def square(x):
    return x**2

def power(x, a):
    return x**a

# Radical functions

def sqrt(x):
    return x**0.5

def root(x, degree):
    return x**(1/degree)

# Rational functions

def reciprocal(x):
    return 1/x

# Trigonometric functions

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

# Inverse trigonometric functions

def arcsin(x):
    return math.asin(x)

def arccos(x):
    return math.acos(x)

def arctan(x):
    return math.atan(x)

# Hyperbolic functions

def sinh(x):
    return math.sinh(x)

def cosh(x):
    return math.cosh(x)

def tanh(x):
    return math.tanh(x)