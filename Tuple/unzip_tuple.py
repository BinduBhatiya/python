# UNZIP THE LIST OF TUPLE DATA

# METHOD 1(using for loop):
test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
print('original list is : ',test_list)
res = [[i for i,j in test_list],[j for i,j in test_list]]
print('unzip the the list of tuple: ',res)

# OUTPUT :
'''
original list is :  [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
unzip the the list of tuple:  [['Akshat', 'Bro', 'is', 'Placed'], [1, 2, 3, 4]]
'''

# METHOD 2(using zip(*)):
test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
print('original list is : ',test_list)
res = list(zip(*test_list))
print('unzip the the list of tuple: ',res)

# OUTPUT :
'''
original list is :  [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
unzip the the list of tuple:  [('Akshat', 'Bro', 'is', 'Placed'), (1, 2, 3, 4)]
'''

