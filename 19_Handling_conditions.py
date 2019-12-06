# Tax system in Canada - if something costs less than 1$, you do not pay tax on it
# E.g. define price = 2.00, print
# Then define price = 0.50, print, and see the diference in the output

# Tip: try to play with the code, add a sentence about taxes etc.

price = 2
if price >= 1.00:
    tax = .07
    print("Tax is: " +  str(tax))
else:
    tax = 0
    print("Tax is: " + str(tax))


# Careful! string comparisons are case sensitive

#1 gives the wrong output! It is a runtime error
country = "CANADA"
if country == "canada":
    print("Oh look a Canadian")
else:
    print("You are not from Canada")
    # Output: You are not from Canada

#2 gives the correct output!
country = "CANADA"
if country.lower() == "canada":
    print("Oh look a Canadian")
else:
    print("you are not from Canada")
    # Output: Oh look a Canadian