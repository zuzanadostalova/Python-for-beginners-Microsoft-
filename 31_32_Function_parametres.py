# 30. and 31. lesson
# We use upper case for ID etc. but for email we do not always need it

# If get_initial(first_name, False) - uppercase is not forced
# get_initial(first_name, True) - uppercase is forced
# def get_initial(name, force_uppercase):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial

# first_name = input("Enter your first name: ")
# first_name_initial = get_initial(first_name, False)

# print("Your initial is: " + first_name_initial)

# You can specify a default value for a parameter
# def get_initial(name, force_uppercase=True):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial

# first_name = input("Enter your first name: ")
# first_name_initial = get_initial(first_name, False)

# print("Your initial is: " + first_name_initial)

# You can assign the values to parametres by name when function is called
# def get_initial(name, force_uppercase):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial

# first_name = input("Enter your first name: ")
# first_name_initial = get_initial(force_uppercase=True, nam   e=first_name)

# print("Your initial is: " + first_name_initial)

# Named notations when calling functions make the code more readable
def error_logger(error_code, error_severity, log_to_db, \
                 error_message, source_module):
    print("Oh no, error: " + error_message)
    # Imagine a code here that logs our error to a database or a file

first_number = 10
second_number = 5
if first_number > second_number:
    error_logger(error_code=45, error_severity=1, 
                 log_to_db=True,
                 error_message="Second number is greater than first",
                 source_module="my_math_method")

