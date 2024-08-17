# What is the difference between summation and addition?
'''
Addition is done between two arguments whereas summation happens over n elements.
'''

# add the value of array1 to the value of array2
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)
print("addition of two array: ",newarr)         # addition of two array:  [2 4 6]


# sum of two array.
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1,arr2])
print("sum of two value: ",newarr)              # sum of two value:  12


# summation over an axis.
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])

newarr = np.sum([arr1,arr2],axis=1)
print("sum using axis: ",newarr)                # sum over axis:  [6 6]


# cumulative sum.
'''
Cummulative sum means partially adding the elements in array.
E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
Perfom partial sum with the cumsum() function.
'''
import numpy as np

arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print("cummulative sum: ",newarr)               # cummulative sum:  [1 3 6]
