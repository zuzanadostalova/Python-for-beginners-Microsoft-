# 38. and 39. lesson - JavaScript Object Notation
# the output of calling API is in JSON
# standard data format 
# picture analyzed through analyze image service
# JSON linters - to read JSON output with code, formatting making it easier
# to read the output

# how to write the code which will read  it?
# JSON contains key pairs - either a key - subkeys, subvalues or key - tags, list of values
# different methods to read through JSON whether it is 1) key - value,
# 2) key - subkeys, 3) key - a list of values

# 1) key - value; request the key name 
# import JSON library
# print(results["requestId"])
# output:"3e06b5ccceec4cd3b5e1112c5b2e5c60"

# 2) key - subkeys; key and subkey name
# print (results["color"]["dominantColorBackground"])
# output:White

# 3) key - a list of values
# print(results["description"]["tags"][0])
# output:bear
