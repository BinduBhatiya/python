# dictionary :
# simple dictionary print

info = {'name':'krishna','age':20,'eligible':True}
print(info)                                             # {'name': 'krishna', 'age': 20, 'eligible': True}

# using list of tuple
places = dict([('ahemdabad',21), ('delhi',22)])
print(places)                                            # {'ahemdabad': 21, 'delhi': 22}

# using list of list
places = dict([['ahemdabad','gandhinagar'], ['delhi','mumbai']])
print(places)                                            # {'ahemdabad': 'gandhinagar', 'delhi': 'mumbai'}   

# using tuple of list
places = dict((['ahemdabad',21], ['delhi',22]))
print(places)                                           # {'ahemdabad': 21, 'delhi': 22}

# using tuple of tuple
places = dict((('ahemdabad',21), ('delhi',22)))
print(places)                                           # {'ahemdabad': 21, 'delhi': 22}

# using tuple of tuple
places = dict(({'ahemdabad',21}, {'delhi',22}))
print(places)                                           # {'ahemdabad': 21, 'delhi': 22}

# using key word parameter
places = dict(a='ahamdabad', b='baroda', c='cat')
print(places)                                           # {'a': 'ahamdabad', 'b': 'baroda', 'c': 'cat'}


# access items :
# access single value

info = {'name':'krishna','age':20,'eligible':True}
print(info['name'])                                     # krishna
print(info.get('eligible'))                             # true

# access multiple value

info = {'name':'krishna','age':20,'eligible':True}
print(info.values())                                    # dict_values(['krishna', 20, True]) 

# access key

info = {'name':'krishna','age':20,'eligible':True}
print(info.keys())                                      # dict_keys(['name', 'age', 'eligible'])

# access key:value pair

info = {'name':'krishna','age':20,'eligible':True}
print(info.items())                                     # dict_items([('name', 'krishna'), ('age', 20), ('eligible', True)])

# copy dictionary
# copy()
# We can use the copy() method to copy the contents of one dictionary into another dictionary.

info = {'name':'krishna','age':20,'eligible':True}
print(info.copy())                                      # {'name': 'krishna', 'age': 20, 'eligible': True}

# dict()
# we can use the dict() function to make a new dictionary with the items of original dictionary.

info = {'name':'krishna','age':20,'eligible':True}
print(dict(info))                                       # {'name': 'krishna', 'age': 20, 'eligible': True}


# add/remove items :

# create a new key and assign a value to it.
info = {'name':'krishna','age':20,'eligible':True}
print(info)                                             # {'name': 'krishna', 'age': 20, 'eligible': True}
info['DOB']=2001
print(info)                                             # {'name': 'krishna', 'age': 20, 'eligible': True, 'DOB': 2001}
info['ID', 'fees']=1, 1000
print(info)                                             # {'name': 'krishna', 'age': 20, 'eligible': True, 'DOB': 2001, ('ID', 'fees'): (1, 1000)}



# update() method
# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
info = {'name':'krishna','age':20,'eligible':True}
print(info)
info.update({'age':21})                                 # {'name': 'krishna', 'age': 20, 'eligible': True}
info.update({'DOB':2001})
print(info)                                             # {'name': 'krishna', 'age': 21, 'eligible': True, 'DOB': 2001}

# clear()
# remove item from dictionary
info = {'name':'krishna','age':20,'eligible':True}
print(info.clear())                                     # None

# pop()
# pop() method remove the key-value pair whose key passed as a parameter.
info = {'name':'krishna','age':20,'eligible':True}
info.pop('eligible')
print(info)                                             # {'name': 'krishna', 'age': 20}

info = {'name':'krishna','age':20,'eligible':True}
print(info.pop('age'))                                  # 20 it return value of key.


# popitem()
# popitem() remove the last key-value pair from dictionary.
info = {'name':'krishna','age':20,'eligible':True}
info.popitem()
print(info)                                             # {'name': 'krishna', 'age': 20}

# apart from these three methods, we can also use the del keyword to remove a dictionary item. 
info = {'name':'krishna','age':20,'eligible':True}
del info['age']
print(info)                                             # {'name': 'krishna', 'eligible': True}

# If key is not provided, then the del keyword will delete the dictionary entirely.
# info = {'name':'krishna','age':20,'eligible':True}
# del info
# print(info)                                           # NameError: name 'info' is not defined


# setdefault()
# This method is used to retrieve the value of a key if it is present; if the key is not present, it inserts the key with a specified default value.

my_dict = {'apple': 1, 'banana': 2}

apple_value = my_dict.setdefault('apple', 10)
print('Apple:', apple_value)  # Output: Apple: 1

cherry_value = my_dict.setdefault('cherry', 5)
print('Cherry:', cherry_value)  # Output: Cherry: 5

print('Updated Dictionary:', my_dict)  
# Output: Updated Dictionary: {'apple': 1, 'banana': 2, 'cherry': 5}


# has_key()
# Here's how you can check 'if' a key exists in a dictionary using the in keyword:

my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}

# Check if 'banana' is a key in the dictionary
if 'banana' in my_dict:
    print('Banana is present in the dictionary')
else:
    print('Banana is not present in the dictionary')

# Check if 'orange' is a key in the dictionary
if 'orange' in my_dict:
    print('Orange is present in the dictionary')
else:
    print('Orange is not present in the dictionary')


# output :
'''
    Banana is present in the dictionary
    Orange is not present in the dictionary
'''


# setdefault()
# This method is used to retrieve the value of a key if it is present; if the key is not present, it inserts the key with a specified default value.

my_dict = {'apple': 1, 'banana': 2, 'orange':''}

apple_value = my_dict.setdefault('orange', 10)
print('orange:', apple_value)  # Output: orange 

