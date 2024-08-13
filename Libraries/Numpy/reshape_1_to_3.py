# reshape numpy array.

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)
newarr = arr.reshape(2, 2, 3)
print(newarr)

'''
    [[[ 1  2][ 3  4][ 5  6]],[[ 7  8][ 9 10][11 12]]]


    [[[ 1  2  3]
    [ 4  5  6]]

    [[ 7  8  9]
    [10 11 12]]]
'''


# convert array into 1D array.

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-2)
print(newarr)       # [1,2,3,4,5,6]


# convert 1D element into 3D array with 2x2 matrix.
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

'''
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
'''