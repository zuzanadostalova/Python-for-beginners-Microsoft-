#If only one of the statements will occur, use elif
# province = input("Enter your province: ")
# if province == "Alberta":
#     tax = 0.05
# elif province == "Nunavut":
#     tax = 0.05
# elif province == "Ontario":
#     tax = 0.13
# print("Tax rate is: " + str(tax))

# Use elif to add a default action
# province = input("Enter your province: ")
# if province == "Alberta":
#     tax = 0.05
# elif province == "Nunavut":
#     tax = 0.05
# elif province == "Ontario":
#     tax = 0.13
# else:
#     tax = 0.15
# print("Tax rate is: " + str(tax))

# Mutltiple conditions by same the action -> combine them into a single one
province = input("Enter your province: ")
if province == "Alberta" \
   or province == "Nunavut":
    tax = 0.05
elif province == "Ontario":
    tax = 0.13
else:
    tax = 0.15
print("Tax rate is: " + str(tax))