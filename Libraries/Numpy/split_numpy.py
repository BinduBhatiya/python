# split the numpy array.

import numpy as np
arr = np.array([1,2,3,4,5,6])
spt = np.array_split(arr,2)
print(spt)          # [array([1, 2, 3]), array([4, 5, 6])]
spt = np.array_split(arr,3)
print(spt)          # [array([1, 2]), array([3, 4]), array([5, 6])]
spt = np.array_split(arr,4)
print(spt)          # [array([1, 2]), array([3, 4]), array([5]), array([6])]



import numpy as np
arr = np.array([1,2,3,4,5,6])
spt = np.array_split(arr,3)
print(spt[0])   # [1 2]
print(spt[1])   # [3 4]
print(spt[2])   # [5 6]



import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print("====>",newarr)

# output :
'''
    [array([[ 1],[ 4],[ 7],[10],[13],[16]]), 
    array([[ 2],[ 5],[ 8],[11],[14],[17]]), 
    array([[ 3],[ 6],[ 9],[12],[15],[18]])]
'''


import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)      # it return output without using "axis" argument. it does not support.
print("------>",newarr)

# output :
'''
    [array([[ 1],[ 4],[ 7],[10],[13],[16]]), 
    array([[ 2],[ 5],[ 8],[11],[14],[17]]), 
    array([[ 3],[ 6],[ 9],[12],[15],[18]])]
'''