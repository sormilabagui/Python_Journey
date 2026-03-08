#demonstrating generators in python

def fibonacci_gen():
    a, b =0, 1
    while True:
        yield a
        a, b = b, a + b

#using the generator
fib = fibonacci_gen()

print("first 10 fibonacci numbers:")

for _ in range(10):
    print(next(fib))