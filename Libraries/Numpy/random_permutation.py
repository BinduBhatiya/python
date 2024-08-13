# print value from array using suffle().

from numpy import random
import numpy as np
arr = np.array([2,4,6,8,10])
random.shuffle(arr)
print("using shuffle : ",arr)      # [2 10 4 8 6] it is generate random value from given array.


# print value from array using permutation.

from numpy import random
import numpy as np
arr = np.array([10,20,30,40,50])
new = random.permutation(arr)  # [30,20,50,10,40] print value.
print("Random permutation : ",new)


# note :
'''
The difference between shuffle and permutation is where using shuffle then it changes on original array. whereas, in permutation we can't changes in original array. 
'''