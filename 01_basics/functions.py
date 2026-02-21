#user-defined functions

def greet_user(name):
    return f"Hello, {name}! welcome back..."

def calculate_bmi(weight,height):
    bmi= weight/(height**2)
    return round(bmi,2)

def check_even_odd(n):
    if n%2==0:
        return "even"
    return "odd"

#function calls
print(greet_user("buddy"))
print("BMI:",calculate_bmi(60,1.65))
print("Number is ",check_even_odd(7))
