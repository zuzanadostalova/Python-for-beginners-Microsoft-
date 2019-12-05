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
