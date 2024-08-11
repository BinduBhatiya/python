# searching in numpy array.
import numpy as np
arr = np.array([1,2,3,4,5,6])
x = np.where(arr == 4)
print(x)            # (array([3], dtype=int64),)


# Find the indexes where the values are even:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)            # (array([1, 3, 5, 7], dtype=int64),)


# searchsorted() :
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)        # 1


import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)        # 2