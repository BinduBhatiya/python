# chdir()
# Change the current working directory

import os
current_directory = os.getcwd()
os.chdir("/Users")
new_directory = os.getcwd()

# Verify the change
print("Changed Working Directory:", os.getcwd())


# Changed Working Directory: c:\Users