# HOW TO CLEAR TUPLE DATA.

# using list & clear :
tup = (1,2,3,4,5)
print('original tuple is: ',tup)
res = list(tup)
res.clear()
print(res)
clr = tuple(res)
print('clearing tuple: ',clr)

# OUTPUT :
'''
original tuple is:  (1, 2, 3, 4, 5)
[]
clearing tuple:  ()
'''

# using del keyword :
tup = (1,2,3,4,5)
print('original tuple is: ',tup)
del tup
#print('deleted tuple: ',tup)                    # NameError: name 'tup' is not defined


# using * operator :
tup = (1,2,3,4,5)
print('original tuple is: ',tup)
res = (tup) * 0
print('clearing tuple: ',res)

# OUTPUT :
'''
original tuple is:  (1, 2, 3, 4, 5)
clearing tuple:  ()
'''

# using () operator :
tup = (1,2,3,4,5)
print('original tuple is: ',tup)
tup = tuple()
print('clearing tuple: ',tup)

# OUTPUT :
'''
original tuple is:  (1, 2, 3, 4, 5)
clearing tuple:  ()
'''