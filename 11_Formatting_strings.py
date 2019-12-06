# 11. and 12. lesson - Formatting strings

# custom string formatting
first_name = "Christopher"
last_name = "Harrison"

# Try to print all of the string options I.-IV. one after the other
# by commenting them out / uncommenting them
# I. formatting option
output = "Hello, " + first_name + " " + last_name

# II. formatting option
# output = "Hello, {} {}".format(first_name, last_name)

# III. formatting option
# output = "Hello, {0} {1}".format(first_name, last_name)

# IV. formatting option
# line 12 only possible in Python 3
# output = f"Hello, {first_name} {last_name}" 
print(output)

# as you can see, the output is the same for each one of the four options
# there are multiple ways for doing the same types of string concatenation, the choice is yours