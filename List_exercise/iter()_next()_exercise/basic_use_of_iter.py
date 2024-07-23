# WHAT IS THE USE OF "iter()" AND "next()" IN PYTHON
# in simple way it is used to fetch data from iterable.

# EXERCISE 1:
lst = [1,2,3,4,5]
res = iter(lst)

print(next(res))
print(next(res))
print(next(res))

# OUTPUT :
'''
    1
    2
    3
'''

# EXERCISE 2:
lst = [1,2,3,4,5]
res = iter(lst)
for i in range(len(lst)):
    print(next(res))

# OUTPUT :
'''
    1
    2
    3
    4
    5
'''


# EXERCISE 3:
lst = [1,2,3,4,5]
res = iter(lst)
print(list(res))                            # [1,2,3,4,5]
print(res)                                  # <list_iterator object at 0x000002AB5882BFD0>

# OUTPUT :
'''
    [1, 2, 3, 4, 5]
'''


# EXERCISE 4:
lst = ['hello', 'python']
res = iter(lst)
for i in range(len(lst)):
    print(next(res))

# OUTPUT :
'''
    hello
    python
'''