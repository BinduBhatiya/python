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


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# UNPACK NESTED TUPLE

test_list = [(4, (5, 'Gfg')), (7, (8, 6))]
print("The original list is : " + str(test_list))

# Unpacking nested tuples using nested loops
res = []
for z, x in test_list:
	temp = [z]
	for item in x:
		temp.append(item)		# this logic is only used for this test_list value.
	res.append(temp)
	
print("The unpacked nested tuple list is : " + str(res))

# OUTPUT :
'''
The original list is : [(4, (5, 'Gfg')), (7, (8, 6))]
The unpacked nested tuple list is : [[4, 5, 'Gfg'], [7, 8, 6]]
'''

