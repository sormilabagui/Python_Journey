#demonstrating list, set and dictionary comprehension

marks = [45, 78, 90, 33, 67, 90, 78]

#list comprehension: filtering passsed students
passed_mark = [m for m in marks if m >= 50]
print("passed marks: ",passed_mark)

#set comprehension: union passed marks
unique_passed = {m for m in marks if m >= 50}
print("unique passed marks:", unique_passed)

#dictionary comprehension: marks -> result
result_status = {m: ("pass" if m >= 50 else "fail") for m in marks}
print("Result stauts:")
for k,v in result_status.items():
    print(k, ":", v)