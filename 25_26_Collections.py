# 25. and  26. lesson - Collections

# group of items stored inside a column, group with a common name, arrays, dictionary

# List - collection of items, [], any data type I want - external, numbers...
#      - a shopping cart, any type of items all together, integer
#      - guaranteed order, collections are zero-indexed
names = ["Christopher", "Susan"]
print(names)

# Empty list - if I do not know the values beforehand
scores = []
scores.append(98) # add new item to the end
scores.append(99)
print(scores)
print(scores[1]) 

# Array - for machine learning, float, all of the items have to be the same type
from array import array
scores = array("d")
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

# Common operations
names = ["Susan", "Christopher"]
print(len(names)) #get the number of items
names.insert(0, "Bill") # insert before index
print(names)
names.sort()
print(names)

# Retrieving ranges
names = ["Susan", "Christopher", "Bill"]
presenters = names[0:2] # Get the first two items
# Starting index and number of items to retrieve
print(names)
print(presenters)

# Dictionary - key/value pairs, storage order not guaranteed
person = {"first": "Christopher"}
person["last"] = "Harrison"
print(person)
print(person["first"])