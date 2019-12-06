# 13. and 14. lesson
# numbers can be stored in variables

# Getting to know your way around calculations in Python, the use of double asterix for exponent
pi = 3.14159
print(pi)

first_num = 6
second_num = 2
print(first_num + second_num)
print(first_num ** second_num)

# Python gets confused if strings are combined with numbers
days_in_February = 28
print(days_in_February + " total days in February")

# try to print line 15 -> error, you are adding a whole number = integer (e.g 1, 2, 3)
# to a string; you have to put str() before the variable carrying an integer
# comment line 15 out and uncomment line 21 instead, print it - it works!

# print(str(days_in_February) + " total days in February")

# Conversely, when you are adding two strings containing integers, the integeres are treated 
# as strings and you get the wrong result; you have to put int() in front of the variable
# or float(); float is a number with decimal places(1.0, 2.5., 3.6) ()
first_num = "5"
second_num = "6"
print(first_num + second_num)
# print(int(first_num) + int(second_num))
# print(float(first_num) + float(second_num))

# Another form
first_num = input("Please enter a number ")
second_num = input("Please enter another number ")
print(int(first_num) + int(second_num))
print(float(first_num) + float(second_num))

