# f = open("C:\\Users\\Bindu Bhatiya\\Desktop\\Python\\File Handling\\Delete File\\A.txt","x")
# print("file craeted successfully...")

import os
if os.path.exists("C:\\Users\\Bindu Bhatiya\\Desktop\\Python\\File Handling\\Delete File\\A.txt"):
    os.remove("C:\\Users\\Bindu Bhatiya\\Desktop\\Python\\File Handling\\Delete File\\A.txt")
    print("file deleted successfully.")
else:
    print("file not found")

