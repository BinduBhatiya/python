# ITERATE DATA FROM NESTED lIST

# METHOD 1 (using simple for loop) :
lst = [[1,2,3], [4,5,6], [7,8,9]]

for sublst in lst:
    for item in sublst:
        print(item,end=' ')
    print()

# OUTPUT :
'''
    1 2 3 
    4 5 6 
    7 8 9 
'''


# METHOD 2 (using list comprehension) :
lst = [[1,2,3], [4,5,6], [7,8,9]]
result = [item for sublst in lst for item in sublst]
print(result)

# OUTPUT :
'''
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''