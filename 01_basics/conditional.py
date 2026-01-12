#conditional statements

# first program to check odd and even
num = int(input("enter a number to check whether it is even or odd: "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#program to check whether num is pov, neg or 0
if num == 0:
    print(f"{num} is 0")
elif num>0:
    print(f"{num} is positive")
elif num<0:
    print(f"{num} is negative")
else:
    print("invalid")