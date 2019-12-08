# 35. and 36. lesson - VE packages
import helpers
helpers.display("Good", True)

# When we add True - This is a warning is printed out

# To make display available always -> output is the same
from helpers import display
display("Night")

# # Setting a virtual environment
# # Installing a package into there - virtualenv <folder_name>
# # https://docs.python.org/3/tutorial/venv.html

# # Create environment
# python3 -m venv tutorial-env
# # Activate - I will see ('tutorial-env':venv)
# source tutorial-env/bin/activate

# ? pip install --upgrade pip
# python3 -m pip install --user --upgrade pip

# # Installs colorama once
# pip install colorama
# # Installs colorama permanently - I need to create requirements.txt
# pip install -r requirements.txt



