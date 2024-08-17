# product :
# To find the product of the elements in an array, use the prod() function.

import numpy as np

arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print("product is: ",x)     # product is:  24


import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print("product value of 2D array: ",x)      # product value of 2D array:  40320


# using axis.
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2], axis=1)
print("using axis: ",newarr)                # using axis:  [  24 1680]


# cummulative product.
'''
Cummulative product means taking the product partially.
E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]
Perfom partial sum with the cumprod() function.
'''

import numpy as np

arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print("cummulative product: ",newarr)       # cummulative product:  [   5   30  210 1680]