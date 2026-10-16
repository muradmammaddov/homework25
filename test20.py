student_id = input("Enter student id: ")
if len(student_id) != 8 or student_id.isdecimal() == False:
    print("Invalid student id")
else:
    print("Student ID accepted")