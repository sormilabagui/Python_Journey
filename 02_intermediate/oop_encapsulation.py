#demonstrating encapsulation using a student grade manager

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    #getter method
    def get_marks(self):
        return self.__marks
    
    #setter method
    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
            print("Marks updated successfully")
        else:
            print("Invalid marks! Must be between 0 and 100")

    #method to calculate grade
    def calculate_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 50:
            return "C"
        else:
            return "Fail"
        

student1 = Student("Arshi", 82)

print("Marks:", student1.get_marks())
print("Grade:", student1.calculate_grade())

student1.update_marks(95)

print("Updaed Msrks:", student1.get_marks())
print("Update Grade:", student1.calculate_grade())