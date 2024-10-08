# it will get the shape of array.

import numpy as np
arr = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])
print(arr.shape)    # (2,4)


import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)          # [[[[[1 2 3 4]]]]]
print('shape of array :', arr.shape)    # shape of array : (1, 1, 1, 1, 4)