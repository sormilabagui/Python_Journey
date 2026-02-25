# demonstrating exception handling with practical example

def safe_division(a, b):
    try:
        result = a / b
        print("result:", result)

    except ZeroDivisionError:
        print("error: cannot divide by zero")

    except TypeError:
        print("error: invalid data type provided")

    else:
        print("division successful")

    finally:
        print("Operation completed. \n")


safe_division(10, 2)
safe_division(5, 0)
safe_division(8, "a")