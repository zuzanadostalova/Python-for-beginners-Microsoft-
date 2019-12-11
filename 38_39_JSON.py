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
# output:bear -  we want all of the tags that came back -> loop: 
# for item in results["description"]["tags"]:
#     print(item)
#     print(item)
# output:
# bear
# polar
# animal
# mammal
# outdoor
# water
# white
# large
# snow
# standing
# eating
# walking
# field
# enclosure

# Creating a JSON tool
# 1) create "key":"value" JSON objects from a dictionary
# create a dictionary object
import json
person_dict = {"first":"Christopher", "last":"Harrison"}
# add additional key pairs as needed to dictionary
person_dict["City"]="Seattle"

# # Convert dictionary to JSON 
# person_json = json.dumps(person_dict)
# print(person_json)
# # -> three key - value pairs

# 2) create "key":"subkey" JSON objects from nest dictionaries
# person_dict = {"first":"Christopher", "last":"Harrison"}
# # create staff dict which assigns a person to a role
# staff_dict = {}
# staff_dict["Program  Manager"]=person_dict

# # Convert dictionary to JSON object
# staff_json = json.dumps(staff_dict)

# # Print JSON object
# print(staff_json)

# 3) create "key":list; add lists to the dict to create JSON 
# person_dict = {"first":"Christopher", "last":"Harrison"}

# # create a list object of programming languages
# languages_list = ["CSharp","Python","JavaScript"]
# # add list to dict
# person_dict["languages"] = languages_list

# # Convert dict to JSON object
# person_json = json.dumps(person_dict)
# print(person_json)