# dictionary :
# simple dictionary print

info = {'name':'krishna','age':20,'eligible':True}
print(info)                                             # {'name': 'krishna', 'age': 20, 'eligible': True}

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

