# METHOD 1 (using "+" operator) :

lst = ['hello','python','world']
res = ''
for i in lst:
    res = res +" "+ i
print(res)  

# OUTPUT :
'''
    hello python world
'''

# METHOD 2 (using list comprehension method) :

lst = ['hello','python','world']
res = ' '.join(item for item in lst)  
print(res)

# OUTPUT :
'''
    hello python world
'''

# METHOD 3 (using join method) :

lst = ['hello','python','world']
l = ' '.join(lst) 
print(l)

# OUTPUT :
'''
    hello python world
'''

# METHOD 4 (using "map" method) :

lst = ['hello','python','world']
l = ' '.join(map(str,lst)) 
print(l)

# OUTPUT :
'''
    hello python world
'''