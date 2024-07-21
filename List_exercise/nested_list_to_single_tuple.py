# COVERT NESTED LIST TO SINGLE TUPLE

test_list = [[5, 6], [4, 7, 10], [12], [9, 11]]

print('nested list is: ',str(test_list))

res = [(j, ) for i in test_list for j in i]

print('after converted into single tuple: ',str(res))

# OUTPUT :
'''
nested list is:  [[5, 6], [4, 7, 10], [12], [9, 11]]
after converted into single tuple:  [(5,), (6,), (4,), (7,), (10,), (12,), (9,), (11,)]
'''


