# 29. and 30. lesson Functions
# import datetime
# # Print timestamps to see how long sections of code take to run

# first_name = "Susan"
# print("task completed")
# print(datetime.datetime.now())
# print()

# for x in range(0,10):
#       print(x)
# print("task completed")
# print(datetime.datetime.now())
# print()

# We can use a function instead of repeating code
# import datetime
# # Print the current time
# # Line 21 - a definition of a print time function, def ():
# # afterwards we write the code we want executed when the function is called
# # def print_time():
# #     print("task completed")
# #     print(datetime.datetime.now())
# #     # We are calling now function of the datetime object from the datetime library
# #     print()

# # first_name = "Susan"
# # print_time()

# # for x in range(0,10):
# #     print(x)
# # print_time()

# # The advantages of using function:
# # The code is more readable and easier to update just the created function
# from datetime import datetime
# def print_time():
#     print("task completed")
#     print(datetime.now())
#     print()
# first_name = "Susan"
# print_time()

# for x in range(0,10):
#     print(x)
# print_time()

# If you a different messages to be displayed each time
# pass the task name as a parameter, parameters = flexibility
# from datetime import datetime
# def print_time(task_name):
#     print(task_name)
#     print(datetime.now())
#     print()

# first_name = "Susan"
# print_time("First name assigned")

# for x in range(0,10):
#     print(x)
# print("Loop completed")

# Code looking differently but is based on the same logic
# first_name = input("Enter your first name: ")
# first_name_initial = first_name[0:1]
# last_name = input("Enter your last name: ")
# last_name_initial = last_name[0:1]

# print("Your initials  are: " + first_name_initial + last_name_initial)

person = input("name,surname: ")
info_person = person.split(",")
name = info_person[0]
name_initial = name[-1]
surname = info_person[1]
surname_initial = surname[-1]
print(person)
print(info_person)
print(name)
print(surname)
print(name_initial)
print(surname_initial)