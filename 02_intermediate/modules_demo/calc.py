#this file acts as a custom module

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if b == 0:
        return "cannot divide by zero..."
    return a/b