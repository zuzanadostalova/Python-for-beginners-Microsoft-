# 40. and 41. lesson - Managing keys
# For Windows
import os
os_version = os.getenv("OS")
print(os_version)

# Using dotenv (.env)
# to manage external things to our app, db connection strings, keys, passwords
# store environmental variables in text file
# do not check sensitive values into source control
# .env file
DATABASE=Sample_Connection_String

# app.py
from dotenv import load_dotenv
import os
load_dotenv
database = os.getenv(DATABASE)
print(database)
