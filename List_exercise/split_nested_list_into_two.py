# SPLIT NESTED LIST INTO TWO LIST

# METHOD 1 :
ini_list = [[1, 2], [4, 3], [45, 65], [223, 2]]

print('simple list is : ',ini_list)

res1 = [i[1] for i in ini_list]
res2 = [i[0] for i in ini_list]

print('split nested list is: ',res1,'\n',res2)

# OUTPUT :
'''
simple list is :  [[1, 2], [4, 3], [45, 65], [223, 2]]
split nested list is:  [2, 3, 65, 2] [1, 4, 45, 223]
'''
