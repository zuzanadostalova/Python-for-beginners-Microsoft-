#  36. lesson - Calling an API
# Web service - place there a function
# sharing the functionality, not the actual code
# programmer with the function's address and permission can call it

# Computer vision API - v2.0, analyzing image - we pass an image 
# and AI tells us what is inside
# We need the adress of API and a key = password
# http://Contoso/analyze ... server and method

# Request posts
# I. key
# II. address 
# III. function_parameters 
# IV. message_body
# V. http_headers



# 37.lesson -Calling an API


# This code will show you how to call the Computer Vision API from Python
# You can find documentation on the Computer Vision Analyze Image method here
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# Use the requests library to simplify making a REST API call from Python 
import requests

# We will need the json library to read the data passed back 
# by the web service
import json

# I. key
# You need to update the SUBSCRIPTION_KEY to 
# they key for your Computer Vision Service
SUBSCRIPTION_KEY = "3e06b5ccceec4cd3b5e1112c5b2e5c60"

# II. address
# You need to update the vision_service_address to the address of
# your Computer Vision Service
vision_service_address = "https://pythonimageana.cognitiveservices.azure.com/vision/v2.0/"

# Add the name of the function you want to call to the address
address = vision_service_address + "analyze"

# III. function_parameters
# According to the documentation for the analyze image function 
# There are three optional parameters: language, details & visualFeatures
parameters  = {'visualFeatures':'Description,Color',
               'language':'en'}

# IV. message_body
# Open the image file to get a file object containing the image to analyze
image_path = "./PolarBear/PolarBear.jpg"
image_data = open(image_path, "rb").read()

# V. http_headers - using octet-stream  
# According to the documentation for the analyze image function
# we need to specify the subscription key and the content type
# in the HTTP header. Content-Type is application/octet-stream when you pass in a image directly
headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

# According to the documentation for the analyze image function
# we use HTTP POST to call this function
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))
