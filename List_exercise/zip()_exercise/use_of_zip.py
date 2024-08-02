# SIMPLE USE OF ZIP IN PYTHON.

# EXERCISE 1:
list1 = [1,2,3]
list2 = ['a','b','c']

res = zip(list1,list2)
print(list(res))                                        # [(1, 'a'), (2, 'b'), (3, 'c')]


# EXERCISE 2:
list1 = [1,2,3]
list2 = ['a','b']

res = zip(list1,list2)
print(list(res))                                        # [(1, 'a'), (2, 'b')]

# EXERCISE 3:
list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [1.1,1.2,1.3]

res = zip(list1,list2,list3)
print(list(res))                                        # [(1, 'a', 1.1), (2, 'b', 1.2), (3, 'c', 1.3)]

# EXERCISE 4:
lst = [[1,2,3],[4,5,6],[7,8,9]]
lst1,lst2,lst3 = zip(*lst)
print(lst1)
print(lst2)
print(lst3)


# OUTPUT :
'''
    (1, 4, 7)
    (2, 5, 8)
    (3, 6, 9)
'''

# EXERCISE 5:
list1 = [1,2,3]
list2 = ['a','b','c']

for num,chr in zip(list1,list2):
    print(num,'->',chr)

# OUTPUT :
'''
    1 -> a
    2 -> b
    3 -> c
'''

# EXERCISE 6:
key = ['name','age','salary']
value = ['BINDU','22','10000']

res = dict(zip(key,value))
print(res)

# OUTPUT :
'''
    {'name': 'BINDU', 'age': '22', 'salary': '10000'}
'''


