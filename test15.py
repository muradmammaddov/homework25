exam_score = int(input("Enter exam score: "))
school_score = int(input("Enter school score: "))
age = int(input("Enter age: "))
if age < 0 or (exam_score < 0 or exam_score > 700) or (school_score < 0 or school_score > 100):
    print("Rejected")
elif age < 16:
    print("Rejected")
else:
    if exam_score >= 600 and exam_score <= 700:
        print("Scholarship")
    elif exam_score >= 450 and exam_score <= 599:
        print("Accepted")
    elif exam_score >= 300 and exam_score <= 449:
        if school_score >= 80:
            print("Accepted")
    elif exam_score < 300:
        print("Rejected")
