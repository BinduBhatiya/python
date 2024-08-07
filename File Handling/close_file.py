try:
    f = open("C:\\Users\\Bindu Bhatiya\\Desktop\\Python\\File Handling\\Create File\\newfile.txt","r")
    f.read(5)
except:
    print("Oops,file not found..!")
else:
    f.close()
    print("file is closed.")

# output :
# file is closed.

