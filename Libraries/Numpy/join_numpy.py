# how to conate two numpy array.

# using concatenate() method.
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

cnt = np.concatenate((arr1,arr2))
print(cnt)                              # [1 2 3 4 5 6]


import numpy as np
arr1 = np.array([[1,2,3],[7,8,9]])
arr2 = np.array([[4,5,6],[10,11,12]])

cnt = np.concatenate((arr1,arr2), axis=1)
print(cnt)  


# output :
'''
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]]
'''


# joining array using stack.

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([7,8,9])
cnt = np.stack((arr1,arr2),axis=1)
print(cnt)

# output :
'''
    [[1 7]
     [2 8]
     [3 9]]
'''


# joining array using vstack.

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([7,8,9])
cnt = np.vstack((arr1,arr2))    # it does not support axis keyword as argument.
print(cnt)

# output :
'''
    [[1 2 3]
     [7 8 9]]
'''


# joining array using dstack.

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([7,8,9])
cnt = np.dstack((arr1,arr2))    # it does not support axis keyword as argument.
print(cnt)

# output :
'''
    [[[1 7]
     [2 8]
     [3 9]]]
'''