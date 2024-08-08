# how to create a generator using function.

def gen():
    yield 1
    yield 2
    yield 3

for value in gen():
    print(value)


# output :
'''
    1
    2
    3
'''