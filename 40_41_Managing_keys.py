# 40. and 41. lesson - Managing keys
# For Windows
# import os
# os_version = os.getenv("OS")
# print(os_version)

# Using dotenv (.env)
# to manage external things to our app, db connection strings, keys, passwords
# store environmental variables in text file
# do not check sensitive values into source control
# .env file
# DATABASE=Sample_Connection_String

# app.py
# from environ import load_environ
# load_environ()
import os
db_user=os.environ.get("DB_USER")
db_password=os.environ.get("DB_PASS")
print(db_user)
print(db_password)
# print(os.environ)
# password = os.environ("PASSWORD")
# database = os.getenv(DATABASE)

# print(password)

# 1) create virtual environment
# 2) requirement.txt file with python-dotenv inside
# 3) pip3 install -r requirement.txt in the terminal in virtual environment set up previously
# 4) .env key value pairs we are going to use = password
# 5) .gitignore ... .env
 

