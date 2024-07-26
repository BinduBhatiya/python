# set all topics :
# create set

set1 = {'abc',11,'xyz',12,'pqr'}
print(set1)                                                 # {'pqr', 'xyz', 11, 12, 'abc'}
print(type(set1))                                           # <class 'set'>


# accessing set from using for loop.
set1 = {'abc',11,'xyz',12,'pqr'}
for item in set1:
    print(item)                                             # abc,xyz,pqr,11,12


# add item to set 
set1 = {'abc',11,'xyz',12,'pqr'}
set1.add('bindu')
print(set1)                                                 # {'abc', 'xyz', 'pqr', 11, 12, 'bindu'}

# if you want to add multiple item then you can create two sets and after you can use "update()" method.
set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'lakhu','krishna','ganesh'}
set1.update(set2)
print(set1)                                                 # {'abc', 'pqr', 'lakhu', 'krishna', 'xyz', 11, 12, 'ganesh'}



# remove item from set
# we can use "remove()" and "discard()" method for remove item.
set1 = {'abc',11,'xyz',12,'pqr'}
set1.remove('pqr')
print(set1)                                                 # {'xyz', 'abc', 11, 12}
set1.discard(12)
print(set1)                                                 # {'abc', 'xyz', 11}

# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.
set1 = {'abc',11,'xyz',12,'pqr'}
#set1.remove(10)
print(set1)                                                 # KeyError: 10

set1 = {'abc',11,'xyz',12,'pqr'}
set1.discard(10)
print(set1)                                                 # {'abc', 'pqr', 11, 12, 'xyz'}




# some important methods of set 

# isdisjoint()
# The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'krishna','abc','xyz','ganesh'}
print(set1.isdisjoint(set2))                               # false

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'krishna','ganesh'}
print(set1.isdisjoint(set2))                               # true


# issuperset()
# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'krishna','abc','xyz','ganesh'}
print(set1.issuperset(set2))                               # false

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'abc',11}
print(set1.issuperset(set2))                               # true


# issubset()
# The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'krishna','abc','xyz','ganesh'}
print(set2.issubset(set1))                               # false

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'abc',11}
print(set2.issubset(set1))                               # true




# join Sets :

# union() and update()
# The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'krishna','abc','xyz','ganesh'}
set3 = set1.union(set2)         # it is support in "union()" only.
print(set3)

set1.union(set2)
print(set1)                                         # {11, 12, 'krishna', 'abc', 'pqr', 'xyz', 'ganesh'}

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'krishna','abc','xyz','ganesh'}
set3 = set1.update(set2)
print(set3)                                         # none

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'krishna','abc','xyz','ganesh'}
set1.update(set2)
print(set1)                                         # {'pqr', 11, 12, 'xyz', 'abc', 'krishna', 'ganesh'}


# intersection() and intersection_update()
# The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'krishna','abc','xyz','ganesh'}
set3 = set1.intersection(set2)
print(set3)                                         # {'xyz', 'abc'}

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'krishna','abc','xyz','ganesh'}
set1.intersection_update(set2)
print(set1)                                         # {'xyz', 'abc'}


# symmetric_difference() and symmetric_difference_update()
# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'krishna','abc','xyz','ganesh'}
set3 = set1.symmetric_difference(set2)
print(set3)                                         # {'krishna', 'ganesh', 11, 12, 'pqr'}

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'krishna','abc','xyz','ganesh'}
set1.symmetric_difference_update(set2)
print(set1)                                         # {'krishna', 'ganesh', 11, 12, 'pqr'}


# difference() and difference_update()
# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'krishna','abc','xyz','ganesh'}
set3 = set1.difference(set2)
print(set3)                                         # {11, 12, 'pqr'}

set1 = {'abc',11,'xyz',12,'pqr'}
set2 = {'krishna','abc','xyz','ganesh'}
set1.difference_update(set2)
print(set1)                                         # {11, 12, 'pqr'}