# oop_inheritance.py
# Demonstrating inheritance in Object-Oriented Programming

# Parent Class
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")


# Child Class (inherits Student)
class GraduateStudent(Student):
    def __init__(self, name, course, specialization):
        # calling parent constructor
        super().__init__(name, course)
        self.specialization = specialization

    def display_graduate_info(self):
        self.display_info()
        print(f"Specialization: {self.specialization}")


# Creating object
grad_student = GraduateStudent("Arpita", "MCA", "Data Analytics")

grad_student.display_graduate_info()