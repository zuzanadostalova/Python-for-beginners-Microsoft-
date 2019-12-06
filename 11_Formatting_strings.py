# 11. lesson - Formatting strings

# custom string formatting
first_name = "Christopher"
last_name = "Harrison"

output = "Hello, " + first_name + " " + last_name
output = "Hello, {} {}".format(first_name, last_name)
output = "Hello, {0} {1}".format(first_name, last_name)

# line 12 only possible in Python 3
output = f"Hello, {first_name} {last_name}" 