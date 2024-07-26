# HOW TO COPY THE DATA.

# EXERCISE 1(using import 'copy'):
import copy
org_lst = [[1,2,3],4,5]
copy_lst = copy.copy(org_lst)
org_lst[0][2] = 6
copy_lst[0][1] = 5
print('original list is: ',org_lst,id(org_lst))                 # original list is:  [[1, 5, 6], 4, 5] -> 1975077174912
print('copied list is: ',copy_lst,id(copy_lst))                  # copied list is:  [[1, 5, 6], 4, 5] -> 1975077174144


# EXERCISE 2(using without import 'copy'):
org_lst = [[1,2,3],4,5]
copy_lst = org_lst.copy()
org_lst[0][2] = 6
print('original list is: ',org_lst,id(org_lst))                 # original list is:  [[1, 2, 6], 4, 5] -> 1975077175040
print('copied list is: ',copy_lst,id(copy_lst))                 # copied list is:  [[1, 2, 6], 4, 5] ->  1975077174912



# EXERCISE 3(using import 'copy')
from copy import deepcopy 
org_lst = [[1,2,3],4,5]
copy_lst = copy.deepcopy(org_lst)
org_lst[0][2] = 6
print('original list is: ',org_lst,id(org_lst))                 # original list is:  [[1, 2, 6], 4, 5] -> 1975077390336
print('copied list is: ',copy_lst,id(copy_lst))                 # copied list is:  [[1, 2, 3], 4, 5] -> 1975077175040


# EXERCISE 4(using import 'copy'):
import copy
org_lst = [[1,2,3],4,5]
copy_lst = copy.copy(org_lst)
org_lst[0].append(5)
print('original list is: ',org_lst,id(org_lst))                 # original list is:  [[1, 2, 3, 5], 4, 5] -> 2154124410816
print('copied list is: ',copy_lst,id(copy_lst))                 # copied list is:  [[1, 2, 3, 5], 4, 5] -> 2154124626048


# EXERCISE 5(using import 'copy'):
import copy
org_lst = [[1,2,3],4,5]
copy_lst = copy.copy(org_lst)
#org_lst[3].append(7)
print('original list is: ',org_lst,id(org_lst))                 # original list is:  [[1, 2, 3, 5], 4, 5,7] -> 2270315151488
print('copied list is: ',copy_lst,id(copy_lst))                 # copied list is:  [[1, 2, 3, 5], 4, 5] -> 2270315317504



# EXERCISE 6(using append):
original = [1, 2, 3]
copy_lst = []

copy_lst.append(original)
original.append(4)
original.append(5)
copy_lst.append(6)

print(copy_lst)             # Output: [[1, 2, 3, 4, 5],6]
print(original)             # Output: [1, 2, 3, 4, 5]
