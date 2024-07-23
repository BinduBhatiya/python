# SIMPLE USE OF ENUMERATE IN PYTHON LIST.

# EXERCISE 1:
lst = ['banana', 'mango', 'apple', 'guavava', 'strawberry']
for ind, fruit in enumerate(lst):
    print(ind,'->',fruit)

# OUTPUT :
'''
    0 -> banana
    1 -> mango
    2 -> apple
    3 -> guavava
    4 -> strawberry
'''

# EXERCISE 2:
lst = ['banana', 'mango', 'apple', 'guavava', 'strawberry']
for ind, fruit in enumerate(lst,start=1):
    print(ind,'->',fruit)

# OUTPUT :
'''
    1 -> banana
    2 -> mango
    3 -> apple
    4 -> guavava
    5 -> strawberry
'''

# EXERCISE 3:
lst = ['banana', 'mango', 'apple', 'guavava', 'strawberry']
res = list(enumerate(lst))
print(res)

# OUTPUT :
'''
    [(0, 'banana'), (1, 'mango'), (2, 'apple'), (3, 'guavava'), (4, 'strawberry')]
'''