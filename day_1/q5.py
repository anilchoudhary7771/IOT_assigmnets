"""
The marks obtained by a student in 3 different subjects are input by the user. Your program should calculate
the average of subjects and display the grade. The student gets a grade as per the following rules:
Average Grade
90-100 A
80-89 B
70-79 C
60-69 D
0-59 F
"""

math_marks = int(input("Enter the Mathematics obtained marks out of 100: "))
science_marks = int(input("Enter the Science obtained marks out of 100: "))
english_marks = int(input("Enter the English obtained marks out of 100: "))


avg = (math_marks + science_marks + english_marks)/3
if avg >= 90 and avg <= 100:
    print(f"A grade with average = {avg}")
elif avg <= 89 and avg >= 80:
    print(f"B grade with average = {avg}")
elif avg <= 79 and avg >= 70:
    print(f"C grade with average = {avg}")
elif avg <= 69 and avg >= 60:
    print(f"D grade with average = {avg}")
elif avg <= 59  and avg >= 0:
    print(f"F grade with average = {avg}")
else:
    print("Invalid marks..!!")
