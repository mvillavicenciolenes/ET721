"""
Michael Villavicencio
Lab 3, Python review

"""

print("---------------- Example 1: Control Flow -----------------")
labs = int(input("Enter Lab's Grade: "))
exams = int(input("Enter Exam's Grade: "))

# Calculate the final grade based on lab and exam grades
if 0 <= labs <= 100 and 0 <= exams <= 100:  # Check for valid grades
    finalGrade = (labs + exams) / 2
    gpa = ''
    
    # Determine the GPA based on the final grade
    if 100 >= finalGrade >= 90:
        gpa = 'A'
    elif 90 > finalGrade >= 80:
        gpa = 'B'
    elif 80 > finalGrade >= 70:
        gpa = 'C'
    elif 70 > finalGrade >= 60:
        gpa = 'D'
    elif 60 > finalGrade >= 0:
        gpa = 'F'
    else:
        gpa = "UNDEFINED!!!"
else:
    # Handle invalid grades
    if not (0 <= labs <= 100):
        print(f"Grade for lab {labs} is invalid")
    if not (0 <= exams <= 100):
        print(f"Grade for exam {exams} is invalid")
    gpa = 'UNDEFINED'

print(f"Your final grade for the class is {gpa}")
