# EXERCISE 1 :

# code 
list = [10, 20, 30, 40, [80, 60, 70]] 

# Printing sublist at index 4 
print(list[4])                                              # [80, 60, 70]

# Printing 1st element of the sublist 
print(list[4][0])                                           # 80

# Printing 2nd element of the sublist 
print(list[4][1])                                           # 60

# Printing 3rd element of the sublist 
print(list[4][2])                                           # 70


# EXERCISE 2 :

# code 
list = [10, 20, 30, 40, [80, 60, 70]] 

# Printing sublist at index 4 
print(list[-1])                                             # [80,60,70]

# Printing 1st element of the sublist 
print(list[-1][-3])                                         # 80

# Printing 2nd element of the sublist 
print(list[-1][-2])                                         # 60

# Printing 3rd element of the sublist 
print(list[-1][-1])                                         # 70


# EXERCISE 3 :

# code 
# LIST 
list = [["Rohan", 60], ["Aviral", 21], 
		["Harsh", 30], ["Rahul", 40], 
		["Raj", 20]] 

# looping through nested list using indexes 
for names in list: 
	print(names[0], "is", names[1], 
		"years old.") 


# OUTPUT :
'''
    Rohan is 6o years old.
	Aviral is 21 years old.
    Harsh is 30 years old.
    Rahul is 40 years old.
    Raj is 20 years old.
'''

# EXERCISE 4 :

# code 
# list 
list = [10, 20, 30, 40, 
		[80, 60, 70]] 

# print the entire Sublist at index 4 
print(list[4][:])                                               # [80,60,70]

# printing first two element 
print(list[4][0 : 2])                                           # [80,60]


