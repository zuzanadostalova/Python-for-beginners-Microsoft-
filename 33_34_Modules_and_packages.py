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

# 34. lesson Virtual environment
# Install virtual environment, globally - we are always going to need it 
pip install virtualenv

#Windows systems 
python -m venv <folder_name>

# OSX/Linux (bash)
virtualenv <folder_name>

# Using Virtual environment - we need to activate it
# cmd.exe, batch file
<folder_name>\Scripts\Activate.bat
# Powershell
<folder_name>\Scripts\Activate.ps1
# bash shell, . - location of your source code, from the current directory
# that is the syntax you need
. ./<folder_name>/Scripts/activate

# OSX/Linux (bash)
<folder_name>/bin/activate

# Installing packages in VE

# Installing packages, locally
# Install an individual package; colorama changes the color of text when you print
pip install colorama

# Install from a list of packages
pip install -r requirements. txt

# requirements.txt
colorama
