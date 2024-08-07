# copy one file to another file.

try:
    with open("C:\\Users\\Bindu Bhatiya\\Desktop\\Python\\File Handling\\Create File\\newfile.txt","r") as f1:
        with open("C:\\Users\\Bindu Bhatiya\\Desktop\\Python\\File Handling\\Create File\\copyfile.txt","w") as f2:
            for i in f1:
                f2.write(i)
except:
    print("Oops,file not found..!")
else:
    f1.close()
    print("file is closed.")


# output :
# file is closed.

