# how to iterate the data of numpy array.

import numpy as np
arr = np.array([1,2,3,4,5,6])
for x in arr:
    print(x,end=',')            # 1,2,3,4,5,6,


import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)  

'''
[1 2 3]
[4 5 6]
'''


import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    for y in x:
        print(y,end=',')                # 1,2,3,4,5,6,
             


import numpy as np
arr = np.array([[[1,2,3],[4,5,6]]])
for x in arr:
    print(x)  

'''
[[1 2 3]
 [4 5 6]]
'''


import numpy as np
arr = np.array([[[1,2,3],[4,5,6]]])
for x in arr:
    for y in x:
        for z in y:
            print(z,end=',')                 # 1,2,3,4,5,6,



# USING "nditer()"

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for x in np.nditer(arr):
    print(x,end=',')                            # 1,2,3,4,5,6,


# iterating with different size :

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for x in np.nditer(arr[:,::2]):
    print(x,end=',')                            # 1,3,4,6


# iterate value with index

import numpy as np
arr = np.array([1,2,3])
for x in np.nditer(arr):
    print(x,end=',')                                    # 1,2,3


import numpy as np
arr = np.array([1,2,3])
for idx,x in np.ndenumerate(arr):
    print(idx,x) 

# output :
'''
    (0,) 1
    (1,) 2
    (2,) 3
'''


import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for idx,x in np.ndenumerate(arr):
    print(idx,x) 

# output :
'''
    (0, 0) 1
    (0, 1) 2
    (0, 2) 3
    (1, 0) 4
    (1, 1) 5
    (1, 2) 6
'''