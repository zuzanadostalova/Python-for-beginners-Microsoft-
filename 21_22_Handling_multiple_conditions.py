# 4 ways for to express multiple conditions:
# I. The usual use of if for different conditions
province = input("Enter your province: ")
if province == "Alberta":
    tax = 0.05
if province == "Nunavut":
    tax = 0.05
if province == "Ontario":
    tax = 0.13
print("Tax rate is: " + str(tax))

# II. If only one of the statements will be true at the time, you can use elif as well
province = input("Enter your province: ")
if province == "Alberta":
    tax = 0.05
elif province == "Nunavut":
    tax = 0.05
elif province == "Ontario":
    tax = 0.13
print("Tax rate is: " + str(tax))

# III. Mutltiple conditions -> same action -> combine them into a single one
province = input("Enter your province: ")
if province == "Alberta" \
   or province == "Nunavut":
    tax = 0.05
elif province == "Ontario":
    tax = 0.13
else:
    tax = 0.15
print("Tax rate is: " + str(tax))

# IV. In Operator - the cleanest code
province = input("Enter your province: ")
if province in("Alberta", \
               "Nunavut", "Yukon"):
    tax = 0.05
elif province == "Ontario":
    tax = 0.13
else:
    tax = 0.15
print("Tax rate is: " + str(tax))

# Note: you can use elif to add a default action - elif one of the mentioned, else province
province = input("Enter your province: ")
if province == "Alberta":
    tax = 0.05
elif province == "Nunavut":
    tax = 0.05
elif province == "Ontario":
    tax = 0.13
else:
    tax = 0.15
print("Tax rate is: " + str(tax))

# Action depending on a combination of conditions, you can use nested if statements
country = input("Enter the name of your home country:  ")
if country.lower() == "canada":
    province = input("Enter the name of your province: ")
    if province in("Alberta", "Nunavut", "Yukon"):
        tax = 0.05
    elif province == "Ontario":
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0
print("Tax rate is: " + str(tax))
