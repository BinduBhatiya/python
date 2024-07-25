# HOW TO UNPACK THE TUPLE IN PYTHON.

# METHOD 1:
tp = ('DSU',1000,'Krishna')
(college,fees,name) = tp

print('college: ',college)
print('fees: ', fees)
print('name: ',name)

# OUTPUT :
'''
college:  DSU
fees:  1000
name:  Krishna
'''

# METHOD 2:
x, *y, z = (10, "Hello", "Python", "World", 50)
print('x -> ',x)
print('y -> ',*y)
print('z -> ',z)

print()

x, y, *z = (10, "Hello", "Python", "World", 50)
print('x -> ',x)
print('y -> ',y)
print('z -> ',*z)

# OUTPUT :
'''
x ->  10
y ->  Hello Python World
z ->  50

x ->  10
y ->  Hello
z ->  Python World 50
'''

