# 9. and 10. lesson String concepts
# strings can be stored in variables
# variables are placeholders for values

first_name = "Christopher"
print(first_name)

# you can combine strings with plus sign +, it is called concatenation
first_name = "Christopher"
last_name = "Harrison"
print(first_name + last_name)
print("Hello " + first_name + " " + last_name)

# always write variables in lower case with underscore
# do not forget to make space after Hello and to add double quotes so the output would be readable

# to modify a string
sentence = "The dog is named Sammy"
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count("a"))

# functions to format strings - e.g. capitalize the input
# try to type in the input in upper case and see for yourself
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("Hello " + first_name.capitalize() + " " + last_name.capitalize())

# note: if there is a mistake in your code, e.g. if you forgot to define a variable
#       you will see green squiggles


