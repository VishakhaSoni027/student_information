subjects = ("c#", "dsc", "python", "c++", "java")
students = ["visha", "vrusti", "heena"]
student_details = {
    "visha": [80, 85, 90, 88, 92],
    "vrusti": [20, 30, 35, 25, 28],  
    "heena": [95, 96, 94, 98, 97]
}
passed_students = set()
failed_students = set()
topper = ""
highest = 0

for i in students:

    marks = student_details[i]
    total = sum(marks)
    average = total / 5
    if average >= 40:
        passed_students.add(i)
    else:
        failed_students.add(i)
    if average > highest:
        highest = average
        topper = i

name = input("enter student name:")

if name in student_details:
    marks = student_details[name]
    total = sum(marks)
    average = total / 5
    if average >= 40:
        result = "Pass"
    else:
        result = "Fail"
    print("Name :", name)
    print("Subjects :", subjects)
    print("Marks :", marks)
    print("c# :", marks[0])
    print("dsc :", marks[1])
    print("python :", marks[2])
    print("c++ :", marks[3])
    print("java:", marks[4])
    print("Total :", total)
    print("Average :", average)
    print("Result :", result)
else:
    print("Student Not Found")
    
print("\nPassed Students", passed_students)
print("Failed Students", failed_students)
print("Topper", topper)