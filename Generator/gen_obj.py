# how to create object in generator.

def myfunc():
    yield 1
    yield 2
    yield 3

obj = myfunc()

print(next(obj))
print(next(obj))
print(next(obj))


# output :
'''
    1
    2
    3
'''