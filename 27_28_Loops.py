# 27. and 28. lesson - Loops
# Only two loops - for and while
# No need for extraneous syntax
# Different useful functions without overbearing you with the unnecessary information

# I. for
# Loop through a collection
for name in ["Christopher", "Susan"]:
    print(name)

# Looping a number of times - range function
for index in range(0, 2):
    print(index)

# This FOR loop on line 20 is going to have the same output as the WHILE loop on line 30
names = ["Christopher", "Susan"]
print()
for name in names:
    print(name)
print()

# II. while
# Looping with a condition

people = ["Christopher", "Susan"]
print()
index = 0
while index < len(people):
    print(people[index])
    index = index + 1
print()

# Without the condition on line 30, the code is going to run forever