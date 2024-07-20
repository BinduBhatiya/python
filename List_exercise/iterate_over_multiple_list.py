# ITERATE THE DATA FROM MULTIPLE LIST.

# METHOD 1 (using simple for loop) :
lst1 = [1,2,3]
lst2 = ['a','b','c']
lst3 = [4,5,6]

for i in range(len(lst1)):
    print(lst1[i],' ',lst2[i],' ',lst3[i])

# OUTPUT :
'''
    1   a   4
    2   b   5
    3   c   6
'''

# METHOD 2 (using zip function) :

for item1, item2, item3 in zip((1, 2, 3), ('a', 'b', 'c'), (True, False, True)):
	print(item1, item2, item3)

# OUTPUT :
'''
    1 a True
    2 b False
    3 c True
'''
