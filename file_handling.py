# create a file :
# Creating a file is primarily done using the create (x) mode.

file = open("Text1.txt",'x')

# write the content in the file.

file = open("Text1.txt", "w")
file.write("This is an example of file creation.")
file.close