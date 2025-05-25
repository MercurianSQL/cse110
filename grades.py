"""
Author: Marinda Keller
Purpose: Grade Calculator - get code along experience in nested if/else statements. """

#input
grade = ""
percentage = ""
total = int(input("How many points was it possible to earn in this course? "))
points = int(input("How many points did you earn? "))
grade = points / total
percentage = round((grade) * 100)
print (f"You have earned {percentage} percentage points in the class.")
print ()

# find letter
letter = ""
if percentage >= 90:
    letter = "A"
elif percentage >= 80:
    letter = "B"
elif percentage >= 70:
    letter = "C"
elif percentage >= 60:
    letter = "D"
else: 
    letter = "F"
letter = str(letter)

# find mark
mark = ""
if (percentage % 10) >=7 and (letter != "A" and letter != "F"):
    mark = "+"
elif (percentage % 10) <3 and letter != "F":
    mark  = "-"
else:
    mark = ""
print (f"Your grade is {letter}{mark}.")
print ()

# find pass
pass_fail = ""
if (percentage >= 70):
    pass_fail = "passed"
else:
    pass_fail = "failed"
print (f"You have {pass_fail} this course.")
print ()