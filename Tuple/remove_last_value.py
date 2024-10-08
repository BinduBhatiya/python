# HOW TO REMOVE LAST VALUE FROM TUPLE.

# METHOD 1:
tup = ['hello','python','world']
n = len(tup)
del tup[n-1]
print("method 1: ",tup)

# OUTPUT :
# ['hello', 'python']


# METHOD 2:
tup = ('hello','python','world')
tup = list(tup)
tup.pop()
print("method 2: ",tup)

# OUTPUT :
# ['hello', 'python']


# METHOD 3:
tup = ('hello','python','world')
tup = list(tup)
tup.remove(tup[-1])
print("method 3: ",tup)

# OUTPUT :
# ['hello', 'python']

