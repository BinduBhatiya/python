# REMOVE ITEM FROM LIST

# METHOD 1 (using del):
lst = [1,2,3,4,5]
del lst[2]
print(lst)                                                  # [1, 2, 4, 5]

# NOTE : IF ONLY NUMBER IN LIST THEN WE MUST USE "del" WHEREAS IF CHARCTER IN LIST THEN WE CAN USE "remove()".

# METHOD 2 (using remove()) :
lst = ['abc','xyz','pqr','def']
lst.remove('pqr')
print(lst)                                                  # ['abc', 'xyz', 'def']


# METHOD 3 (using list comprehension) :
list1 = [1,2,3,4,5]
list1 = [ele for ele in list1 if ele != 3]
print(list1)                                                # [1, 2, 4, 5]


# METHOD 4 (using discard()) :
list1 = [1,2,3,4,5]
lst = set(list1)
lst.discard(3)
lst1 = list(lst)
print(lst1)                                                 # [1, 2, 4, 5]