# 33. lesson - Modules and packages 
# helpers.py
# def display(message, is_warning=False):
#     if is_warning:
#         print("Warning!!!")
#     print(message)

# 1. option how to import a module
# import helpers
# helpers.display("Not a warning")

# 2. option how to import a module
# from helpers import * 
# display("Not a warning")

# 3. option how to import a module
# from helpers import display
# display("Not a warning")

# Installing packages
# Install an individual package; colorama changes the color of text when you print
pip install colorama

# Install from a list of packages
pip install -r requirements. txt

# Requirements.txt
colorama

# 34. lesson Virtual environment
# Install virtual environment
pip install virtualenv

#Windows systems 
python -m venv <folder_name>

# OSX/Linux (bash)
virtualenv <folder_name>

# Using Virtual environment
# cmd.exe
<folder_name>\Scripts\Activate.bat
# Powershell
<folder_name>\Scripts\Activate.ps1
# bash shell
. ./<folder_name>/Scripts/activate

# OSX/Linux (bash)
<folder_name>/bin/activate