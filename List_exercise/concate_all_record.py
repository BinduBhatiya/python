# METHOD 1 :
# Concatenate All Records

# initialize list
test_list = [('hellopython ', 'is'), (' best', ' for'), (' all', ' world')]

# printing original list
print("The original list : " + str(test_list))

# Concatenate All Records
x = []
for i in test_list:
	x.extend(list(i))
res = " ".join(x)
# printing result
print("The Concatenated elements of list is : " + res)


# OUTPUT :
'''
The original list : [('hellopython ', 'is'), (' best', ' for'), (' all', ' world')]
The Concatenated elements of list is : hellopython  is  best  for  all  world
'''