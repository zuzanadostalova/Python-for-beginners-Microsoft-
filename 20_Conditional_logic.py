price = input("How much did you pay? ")

price = float(price)
if price >= 1.00:
    tax = .07
    print("Tax rate is: " + str(tax))