# 23. and 24. lesson - Complex conditions

# Nested if statement
gpa = float(input("Enter your gpa: "))
if gpa >= .85:
    lowest_grade = float(input("Enter your lowest grade: "))
    if lowest_grade >= .70:
        print("Well done!")

# Sometimes you can combine conditions with AND instead of nesting if  
gpa = float(input("What was your Grade Point Average? "))
lowest_grade = float(input("What was your lowest grade? "))
# or: 
# lowest_grade = input ("What was your lowest grade? ")
# lowest_grade = float(lowest_grade)
if gpa >= .85 and lowest_grade >= .70:
        print("Well done!")

# Check if the conditions for honour roll are met
# Boolean variable can be only True or False (always with capital letters)!
gpa = float(input("What was your Grade Point Average? "))
lowest_grade = float(input("What was your lowest grade? "))

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

# Later in the code if I want to know whether the student is on the honour roll or not
# I will just check the Boolean variable, no quotes, it is not a string!
if honour_roll:
        print("You made honour roll!")
