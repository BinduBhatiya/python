# read file 

f = open("C:\\Users\\Bindu Bhatiya\\Desktop\\Python\\File Handling\\Create File\\newfile.txt","r")
print(f.read(5))    # pass only 5 character.
print(f.readline()) # pass only one line.
print(f.readlines())    # if we have multiple sentences in file then it divivde sentence in "[]". 
print("data is read successfully...")

# output :
'''
    hello
    python world.
    []
    data is read successfully...
'''