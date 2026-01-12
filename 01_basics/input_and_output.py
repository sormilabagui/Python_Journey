#user input

name= input("what is ur name? :")
age = int(input("what is ur age?:"))
year = 2026 - age
print(f"hi {name} u r bone in year {year}")

#program of area of rectangle taking length and breadth from user
# area = l*b
print(f"{name} lets find area of rectangle together")
l = float(input("enter the length of rectangle: "))
b = float(input("enter the breadth of rectangle:"))

area = l * b

print(f"Area of rectangle: {area} cm²")