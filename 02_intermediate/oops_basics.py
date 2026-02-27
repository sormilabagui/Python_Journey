# oop_basics.py
# Demonstrating basic Object-Oriented Programming in Python

class Student:
    # Constructor
    def __init__(self, name, course, skills):
        self.name = name
        self.course = course
        self.skills = skills

    # Method to display student info
    def display_profile(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print("Skills:", ", ".join(self.skills))

    # Method to add a new skill
    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"{skill} added successfully")


# Creating object
student1 = Student("Arpita", "MCA", ["Python", "C"])

student1.display_profile()
print()

student1.add_skill("SQL")
print()

student1.display_profile()