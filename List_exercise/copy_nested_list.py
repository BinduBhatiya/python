# COPY THE NESTED LIST

# METHOD 1 (using list comprehensive method):

# List initialization
Input_list = [[0, 1, 2], [3, 4, 5], [0, 1, 8]]

# comprehensive method
out_list = [ele[:] for ele in Input_list]
# out_list = Input_list                                     # it is referance value

# Printing Output
print("Initial list is:")
print(Input_list)
print("New assigned list is")
print(out_list)

# OUTPUT :
'''
    Initial list is:
    [[0, 1, 2], [3, 4, 5], [0, 1, 8]]
    New assigned list is
    [[0, 1, 2], [3, 4, 5], [0, 1, 8]]
'''


# METHOD 2 (using 'append' method) :

# List initialization
Input_list = [[0, 1, 2], [3, 4, 5]]
Output = []

# Using iteration to assign values
for x in range(len(Input_list)):
	temp = []
	for elem in Input_list[x]:
		temp.append(elem)
	Output.append(temp)

# Printing Output
print("Initial list is:")
print(Input_list)
print("New assigned list is")
print(Output)


# OUTPUT :
'''
    Initial list is:
    [[0, 1, 2], [3, 4, 5]]
    New assigned list is
    [[0, 1, 2], [3, 4, 5]]
'''