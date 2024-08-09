# dimension in arrays.
# a dimension in array is one level of array depth (nested arrays).
# NumPy has a whole sub module dedicated towards matrix operations called "numpy.mat"

# 0-D array :
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

import numpy as np
arr = np.array(11)
print(arr)      # 11


# 1-D array :
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)      # [1, 2, 3, 4, 5]


# 2-D array :
# These are often used to represent matrix or 2nd order tensors.

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# output :
'''
[[1 2 3]
 [4 5 6]]
'''


# 3-D array :
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.These are often used to represent a 3rd order tensor.

import numpy as np
arr = np.array([[[1,2,3],[4,5,6]], [[3,7,9],[2,4,6]]])
print("value of arr:\n ",arr)

# output :
'''
value of arr :
[[[1 2 3]
  [4 5 6]]

 [[3 7 9]
  [2 4 6]]]
'''

# check how many dimension in this array.

import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)   # 0
print(b.ndim)   # 1
print(c.ndim)   # 2
print(d.ndim)   # 3


# higher dimension array.
# An array can have any number of dimensions.When the array is created, you can define the number of dimensions by using the ndmin argument.

import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)          # [[[[[1 2 3 4]]]]]
print('number of dimensions :', arr.ndim)   # number of dimensions : 5