# FIND THE ELEMENT EXIST IN ITEM LIST OR NOT

# METHOD 1 (using 'in' ) :

lst = [1,2,3,4,5,6,7]
fnd = 4

if fnd in lst:
    print(fnd,' exist in List.')
else:
    print(fnd,' Not exist in List.')

# OUTPUT :
'''
    4  exist in List.
'''


# METHOD 2 (using loop() ) :

lst = [1,2,3,4,5,6,7]
fnd = 4

for i in lst:
    if i == fnd:
        print(fnd,'exist in list.')

# OUTPUT :
'''
    4  exist in List.
'''

# METHOD 3 (using count() ) :

lst = [1,2,3,4,5,6,7]
res = lst.count(4)

if res > 0:
    print('exist in list.')
else:
    print('Not exist in list.')


# OUTPUT :
'''
    exist in List.
'''

# METHOD 4 (using find() ) :

lst = [1,2,3,4,5,6,7]
con = str(lst)              # required to convert list into string because find not allowed in List.
res = con.find("4")

if res > -1:
    print('exist in list.')
else:
    print('Not exist in list.')



# OUTPUT :
'''
    exist in List.
'''