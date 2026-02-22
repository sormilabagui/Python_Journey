#Demonstrating list, dictionary, set and tuples with a real-life example


#list: Ordered and mutable
students = ["Arpita", "Aayan", "Riya", "Arjun"]
students.append("Neha")
print("Students list:", students)

# tuple: ordered, immutable(fixed data)
college_info = ("ABC university", "MCA", 2026)
print("College info (tuple):",college_info)

#set : unordered and unique values
language_known = {"Python", "C", "Java", "Python"}
print("Languages known (set):", language_known)

#dictionary:key-value pairs
student_profile = {
    "name": "Arpita",
    "age": 23,
    "course": "MCA",
    "skills": ["Python", "C", "SQL"]
}

print("Student Profile (Dictionary):")
for key,value in student_profile.items():
    print(f"{key} : {value}")