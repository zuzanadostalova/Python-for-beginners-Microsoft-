# Check tax
price = input("How much did you pay? ")

price = float(price)
if price >= 1.00:
    tax = .07
    print("Tax rate is: " + str(tax))

# Add else I.
price = input("How much did you pay? ")

price = float(price)
if price >= 1.00:
    tax = .07
    print("Tax rate is: " + str(tax))
else:
    tax = 0
    print("Tax rate is: " + str(tax))

Add else II.
price = input("How much did you pay? ")

price = float(price)
if price >= 1.00:
    tax = .07
else:
    tax = 0
print("Tax rate is: " + str(tax))

Comparing strings
country = input("Enter the name of your home country:  ")
if country == "canada":
    print("So you must like hockey!")
else:
    print("You are not from Canda")

will not work if you enter first capital letter "Canada"

#How to correct runtime error? ->
country = input("Enter the name of your home country:  ")
if country.lower() == "canada":
    print("So you must like hockey!")
else:
    print("You are not from Canda")
    