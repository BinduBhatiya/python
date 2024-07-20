# METHOD 1 (using for loop) :  
# Concatenate 2 Matrix Row-wise

# initializing lists
test_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
test_list2 = [[1, 3], [9, 3, 5, 7], [8]]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

for i in range(0, len(test_list1)):
	test_list1[i].extend(test_list2[i])
# printing result
print("The concatenated Matrix : " + str(test_list1))


# OUTPUT :
'''
    The original list 1 is : [[4, 3, 5], [1, 2, 3], [3, 7, 4]]
    The original list 2 is : [[1, 3], [9, 3, 5, 7], [8]]
    The concatenated Matrix : [[4, 3, 5, 1, 3], [1, 2, 3, 9, 3, 5, 7], [3, 7, 4, 8]]
'''


# METHOD 2 (using list comprehension + zip) :

# initializing lists
test_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
test_list2 = [[1, 3], [9, 3, 5, 7], [8]]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# zip() combines the results
# list comprehension provides shorthand
res = list(sub1 + sub2 for sub1, sub2 in zip(test_list1, test_list2))

# printing result
print("The concatenated Matrix : " + str(res))

# OUTPUT :
'''
    The original list 1 is : [[4, 3, 5], [1, 2, 3], [3, 7, 4]]
    The original list 2 is : [[1, 3], [9, 3, 5, 7], [8]]
    The concatenated Matrix : [[4, 3, 5, 1, 3], [1, 2, 3, 9, 3, 5, 7], [3, 7, 4, 8]]
'''
